#!/usr/bin/env python3
"""Auth class"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class
        API authentication

        public methods:
            require_auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth:
            check for authentication
            return boolean
        """
        if not path or not excluded_paths:
            return True
        if not len(excluded_paths):
            return True
        if path in excluded_paths or path[-1] == '/':
            return False
        if path[-1] != '/':
            path += '/'
            return True

    def authorization_header(self, request=None) -> str:
        """authorization_header:
            return authorization header request
        """
        if not request:
            return request
        authorization = request.headers.get('Authorization')
        return authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user:
        return: TypeVar
        """
        return None
