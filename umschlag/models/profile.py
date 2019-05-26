# coding: utf-8

"""
    Umschlag OpenAPI

    API definition for Umschlag  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Profile(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'slug': 'str',
        'username': 'str',
        'email': 'str',
        'admin': 'bool',
        'active': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'slug': 'slug',
        'username': 'username',
        'email': 'email',
        'admin': 'admin',
        'active': 'active',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, slug=None, username=None, email=None, admin=None, active=None, created_at=None, updated_at=None):  # noqa: E501
        """Profile - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._slug = None
        self._username = None
        self._email = None
        self._admin = None
        self._active = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if slug is not None:
            self.slug = slug
        self.username = username
        self.email = email
        if admin is not None:
            self.admin = admin
        if active is not None:
            self.active = active
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Profile.  # noqa: E501


        :return: The id of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Profile.


        :param id: The id of this Profile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def slug(self):
        """Gets the slug of this Profile.  # noqa: E501


        :return: The slug of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Profile.


        :param slug: The slug of this Profile.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def username(self):
        """Gets the username of this Profile.  # noqa: E501


        :return: The username of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Profile.


        :param username: The username of this Profile.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def email(self):
        """Gets the email of this Profile.  # noqa: E501


        :return: The email of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Profile.


        :param email: The email of this Profile.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def admin(self):
        """Gets the admin of this Profile.  # noqa: E501


        :return: The admin of this Profile.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this Profile.


        :param admin: The admin of this Profile.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def active(self):
        """Gets the active of this Profile.  # noqa: E501


        :return: The active of this Profile.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Profile.


        :param active: The active of this Profile.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def created_at(self):
        """Gets the created_at of this Profile.  # noqa: E501


        :return: The created_at of this Profile.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Profile.


        :param created_at: The created_at of this Profile.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Profile.  # noqa: E501


        :return: The updated_at of this Profile.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Profile.


        :param updated_at: The updated_at of this Profile.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Profile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
