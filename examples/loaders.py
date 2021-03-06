from quart import Quart, jsonify, request
from quart_jwt_extended import JWTManager, jwt_required, create_access_token

app = Quart(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


# Using the expired_token_loader decorator, we will now call
# this function whenever an expired but otherwise valid access
# token attempts to access an endpoint
@jwt.expired_token_loader
def my_expired_token_callback(expired_token):
    token_type = expired_token["type"]
    return (
        {
            "status": 401,
            "sub_status": 42,
            "msg": "The {} token has expired".format(token_type),
        },
        401,
    )


@app.route("/login", methods=["POST"])
async def login():
    username = (await request.get_json()).get("username", None)
    password = (await request.get_json()).get("password", None)
    if username != "test" or password != "test":
        return {"msg": "Bad username or password"}, 401

    ret = {"access_token": create_access_token(username)}
    return ret, 200


@app.route("/protected", methods=["GET"])
@jwt_required
async def protected():
    return {"hello": "world"}, 200


if __name__ == "__main__":
    app.run()
