from quart import Quart, jsonify, request
from quart_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    jwt_refresh_token_required,
    create_refresh_token,
    get_jwt_identity,
    fresh_jwt_required,
)

app = Quart(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


# Standard login endpoint. Will return a fresh access token and
# a refresh token
@app.route("/login", methods=["POST"])
async def login():
    username = (await request.get_json()).get("username", None)
    password = (await request.get_json()).get("password", None)
    if username != "test" or password != "test":
        return {"msg": "Bad username or password"}, 401

    # create_access_token supports an optional 'fresh' argument,
    # which marks the token as fresh or non-fresh accordingly.
    # As we just verified their username and password, we are
    # going to mark the token as fresh here.
    ret = {
        "access_token": create_access_token(identity=username, fresh=True),
        "refresh_token": create_refresh_token(identity=username),
    }
    return ret, 200


# Refresh token endpoint. This will generate a new access token from
# the refresh token, but will mark that access token as non-fresh,
# as we do not actually verify a password in this endpoint.
@app.route("/refresh", methods=["POST"])
@jwt_refresh_token_required
async def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user, fresh=False)
    ret = {"access_token": new_token}
    return ret, 200


# Fresh login endpoint. This is designed to be used if we need to
# make a fresh token for a user (by verifying they have the
# correct username and password). Unlike the standard login endpoint,
# this will only return a new access token, so that we don't keep
# generating new refresh tokens, which entirely defeats their point.
@app.route("/fresh-login", methods=["POST"])
async def fresh_login():
    username = (await request.get_json()).get("username", None)
    password = (await request.get_json()).get("password", None)
    if username != "test" or password != "test":
        return {"msg": "Bad username or password"}, 401

    new_token = create_access_token(identity=username, fresh=True)
    ret = {"access_token": new_token}
    return ret, 200


# Any valid JWT can access this endpoint
@app.route("/protected", methods=["GET"])
@jwt_required
async def protected():
    username = get_jwt_identity()
    return dict(logged_in_as=username), 200


# Only fresh JWTs can access this endpoint
@app.route("/protected-fresh", methods=["GET"])
@fresh_jwt_required
async def protected_fresh():
    username = get_jwt_identity()
    return dict(fresh_logged_in_as=username), 200


if __name__ == "__main__":
    app.run()
