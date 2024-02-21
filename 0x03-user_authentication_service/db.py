#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database

        Args:
            email (str): The email of the user
            hashed_password (str): The hashed password of the user

        Returns:
            User: The created User object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Find a user in the database by specific attributes
        Args:
            **kwargs: Arbitrary keyword arguments representing the,
                      attributes of the user to search for

        Returns:
            User: The User object that matches the specified attributes

        Raises:
            NoResultFound: If no user with the specified attributes is found
            InvalidRequestError: If the query parameters are invalid
        """
        try:
            # Query the User model with the provided keyword arguments
            user = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            # NoResultFound is raised when the .one(),
            # method doesn't find any matches
            raise NoResultFound()
        except InvalidRequestError:
            # InvalidRequestError is raised when the,
            # query parameters are invalid
            raise InvalidRequestError()
        # If a user was found and no exceptions were raised,
        # we return the user
        return user
