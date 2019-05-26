# Kleister: SDK for Python

[![Build Status](http://cloud.drone.io/api/badges/umschlag/umschlag-python/status.svg)](http://cloud.drone.io/umschlag/umschlag-python)
[![Stories in Ready](https://badge.waffle.io/umschlag/umschlag-api.svg?label=ready&title=Ready)](http://waffle.io/umschlag/umschlag-api)
[![Join the Matrix chat at https://matrix.to/#/#umschlag:matrix.org](https://img.shields.io/badge/matrix-%23umschlag%3Amatrix.org-7bc9a4.svg)](https://matrix.to/#/#umschlag:matrix.org)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bcffce563f304d1ea64fdfd16e5e5e3f)](https://www.codacy.com/app/umschlag/umschlag-python?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=umschlag/umschlag-python&amp;utm_campaign=Badge_Grade)
[![PyPI version](https://badge.fury.io/py/umschlag.svg)](https://badge.fury.io/py/umschlag)

**This project is under heavy development, it's not in a working state yet!**

Where does this name come from or what does it mean? It's quite simple, it's one german word for transshipment, I thought it's a good match as it is related to containers and a harbor.

This repository provides a client SDK for Python. This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0-alpha1
- Package version: 1.0.0-alpha1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen


## Installation


### Install with `pip`

If you want to install a published version, you just need to execute this command to get the SDK installed via `pip`:

```bash
pip install umschlag
```

After the installation you can simply start to import the SDK:

```python
import umschlag
```


### Install with `setuptools`

If you want to install a unpublished version you can simply clone this repository and use `setuptools` to install the SDK:

```bash
python setup.py install --user
```

After the installation you can simply start to import the SDK:

```python
import umschlag
```


## Getting Started

Please follow the [installation](#installation) instructions and then run the following code:

```python
from __future__ import print_function
from pprint import pprint
import time
import umschlag
from umschlag.rest import ApiException


api = umschlag.AuthApi(umschlag.ApiClient(configuration))
auth = umschlag.InlineObject() # InlineObject | 

try:
    # Authenticate an user by credentials
    resp = api.login_user(auth)
    pprint(resp)
except ApiException as e:
    print("Exception when calling AuthApi->login_user: %s\n" % e)

```


## Documentation for endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**login_user**](docs/AuthApi.md#login_user) | **POST** /auth/login | Authenticate an user by credentials
*AuthApi* | [**refresh_auth**](docs/AuthApi.md#refresh_auth) | **GET** /auth/refresh | Refresh an auth token before it expires
*AuthApi* | [**verify_auth**](docs/AuthApi.md#verify_auth) | **GET** /auth/verify/{token} | Verify validity for an authentication token
*ProfileApi* | [**show_profile**](docs/ProfileApi.md#show_profile) | **GET** /profile/self | Retrieve an unlimited auth token
*ProfileApi* | [**token_profile**](docs/ProfileApi.md#token_profile) | **GET** /profile/token | Retrieve an unlimited auth token
*ProfileApi* | [**update_profile**](docs/ProfileApi.md#update_profile) | **PUT** /profile/self | Retrieve an unlimited auth token
*TeamApi* | [**append_team_to_user**](docs/TeamApi.md#append_team_to_user) | **POST** /teams/{team_id}/users | Assign a user to team
*TeamApi* | [**create_team**](docs/TeamApi.md#create_team) | **POST** /teams | Create a new team
*TeamApi* | [**delete_team**](docs/TeamApi.md#delete_team) | **DELETE** /teams/{team_id} | Delete a specific team
*TeamApi* | [**delte_team_from_user**](docs/TeamApi.md#delte_team_from_user) | **DELETE** /teams/{team_id}/users | Remove a user from team
*TeamApi* | [**list_team_users**](docs/TeamApi.md#list_team_users) | **GET** /teams/{team_id}/users | Fetch all users assigned to team
*TeamApi* | [**list_teams**](docs/TeamApi.md#list_teams) | **GET** /teams | Fetch all available teams
*TeamApi* | [**permit_team_user**](docs/TeamApi.md#permit_team_user) | **PUT** /teams/{team_id}/users | Update user perms for team
*TeamApi* | [**show_team**](docs/TeamApi.md#show_team) | **GET** /teams/{team_id} | Fetch a specific team
*TeamApi* | [**update_team**](docs/TeamApi.md#update_team) | **PUT** /teams/{team_id} | Update a specific team
*UserApi* | [**append_user_to_team**](docs/UserApi.md#append_user_to_team) | **POST** /users/{user_id}/teams | Assign a team to user
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /users | Create a new user
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /users/{user_id} | Delete a specific user
*UserApi* | [**delete_user_from_team**](docs/UserApi.md#delete_user_from_team) | **DELETE** /users/{user_id}/teams | Remove a team from user
*UserApi* | [**list_user_teams**](docs/UserApi.md#list_user_teams) | **GET** /users/{user_id}/teams | Fetch all teams assigned to user
*UserApi* | [**list_users**](docs/UserApi.md#list_users) | **GET** /users | Fetch all available users
*UserApi* | [**permit_user_team**](docs/UserApi.md#permit_user_team) | **PUT** /users/{user_id}/teams | Update team perms for user
*UserApi* | [**show_user**](docs/UserApi.md#show_user) | **GET** /users/{user_id} | Fetch a specific user
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /users/{user_id} | Update a specific user


## Documentation for models

 - [AuthToken](docs/AuthToken.md)
 - [AuthVerify](docs/AuthVerify.md)
 - [InlineObject](docs/InlineObject.md)
 - [Profile](docs/Profile.md)
 - [Team](docs/Team.md)
 - [TeamUser](docs/TeamUser.md)
 - [TeamUserParams](docs/TeamUserParams.md)
 - [User](docs/User.md)
 - [UserTeamParams](docs/UserTeamParams.md)


## Documentation For authorization

 All endpoints do not require authorization.


## Security

If you find a security issue please contact umschlag@webhippie.de first.


## Contributing

Fork -> Patch -> Push -> Pull Request


## Authors

* [Thomas Boerger](https://github.com/tboerger)


## License

Apache-2.0


## Copyright

```
Copyright (c) 2018 Thomas Boerger <thomas@webhippie.de>
```
