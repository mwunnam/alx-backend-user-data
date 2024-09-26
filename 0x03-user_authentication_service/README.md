# 0x03-user_authentication_service
#
## Task 2
### Understanding the db code snippet
1. import
    * Create_engine (`from sqlalchemy import create_engine`):
    This makes it possible to create an instance of sqlachemy engine. The engine
    is the starting point for any SQLAlchemy application, allowing for the
    connection to the database.

    * Declarative_base (`from sqlalchemy.ext.declarative import declarative_base`):
    This is used to create a declarative model. it establishes the link between
    Python classes and database. It is used to create a base class for the
    declarative model

    * Sessionmaker (`for sqlalchemy.orm import sessionmaker`):
    This makes it possible to create a new Session. A Session is what manages
    the interations with the database and it is what is used to add, update,
    delete and query data.

    * Session (`from sqlalchemy.orm.session import Session`):
    This class represents a workplace for the database operations. It allows you
    to interact with the database and keeps track of changes made to objects

2. `__init__(self)` method:
    * This is used to set up the database.
    It creates the an engine, used `Base.metadata.drop_all(self._engine)` to clear the dat base
    to ensure that there is a new database for testing purposes
    It also creates a new database schema to make sure that new updates are
    also captured with `Base.metadata.create_all(self._engine)`
    For production purposes it is advice to use tools like Alembic to manage the
    schema through migrations
    __session is set to None to make sure that session is only created when it
    is firsts accessed, implemeting a lazy loading pattern. This way resources
    are saved by creating seesion only when needed.

3.  `_session property` Method:
    * This is a memoized property that returns a Session object.
    If `self.__session` is `None` it creates a new session using `sessionmaker`
    bound to the engine.
    This propert makes sure that there is only one active session at a
    time.(singleton pattern).
