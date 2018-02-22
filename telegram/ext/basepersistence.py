#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2018
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains the BasePersistence class."""


class BasePersistence(object):
    """Interface class for adding persistence to your bot.
    Subclass this object for different implementations of a persistent bot.

    All relevant methods must be overwritten. This means:

    * If :attr:`store_chat_data` is ``True`` you must overwrite :meth:`get_chat_data` and
      :meth:`update_chat_data`.
    * If :attr:`store_user_data` is ``True`` you must overwrite :meth:`get_user_data` and
      :meth:`update_user_data`.
    * If you want to store conversation data with :class:`telegram.ext.ConversationHandler`, you
      must overwrite :meth:`get_conversations` and :meth:`update_conversations`.
    * :meth:`flush` will be called when the bot is shutdown, and must always be overwritten.

    Attributes:
        store_user_data (:obj:`bool`): Optional, Whether user_data should be saved by this
            persistence class.
        store_chat_data (:obj:`bool`): Optional. Whether user_data should be saved by this
            persistence class.

    Args:
        store_user_data (:obj:`bool`, optional): Whether user_data should be saved by this
            persistence class. Default is ``True``.
        store_chat_data (:obj:`bool`, optional): Whether user_data should be saved by this
            persistence class. Default is ``True`` .
    """

    def __init__(self, store_user_data=True, store_chat_data=True):
        self.store_user_data = store_user_data
        self.store_chat_data = store_chat_data

    def get_user_data(self):
        """"Will be called by :class:`telegram.ext.Dispatcher` upon creation with a
        persistence object. It should return the user_data if stored, or an empty
        ``defaultdict(dict)``.

        Returns:
            :obj:`defaultdict`: The restored user data.
        """
        raise NotImplementedError

    def get_chat_data(self):
        """"Will be called by :class:`telegram.ext.Dispatcher` upon creation with a
        persistence object. It should return the chat_data if stored, or an empty
        ``defaultdict(dict)``.

        Returns:
            :obj:`defaultdict`: The restored chat data.
        """
        raise NotImplementedError

    def get_conversations(self, name):
        """"Will be called by :class:`telegram.ext.Dispatcher` when a
        :class:`telegram.ext.ConversationHandler` is added if
        :attr:`telegram.ext.ConversationHandler.persistent` is ``True``.
        It should return the conversations for the handler with `name` or an empty ``dict``

        Args:
            name (:obj:`str`): The handlers name.

        Returns:
            :obj:`dict`: The restored conversations for the handler.
        """
        raise NotImplementedError

    def update_conversations(self, name, conversations):
        """Will be called when a :attr:`telegram.ext.ConversationHandler.update_state`
        is called. this allows the storeage of the new state in the persistence.

        Args:
            name (:obj:`str`): The handlers name.
            conversations (:obj:`dict`): The :attr:`telegram.ext.ConversationHandler.conversations`
                dict to store.
        """
        raise NotImplementedError

    def update_user_data(self, user_data):
        """Will be called by the :class:`telegram.ext.Dispatcher` after a handler has
        handled an update. It will be the :attr:`telegram.ext.Dispatcher.user_data` defaultdict.

        Args:
            user_data (:obj:`defaultdict`): The :attr:`telegram.ext.dispatcher.user_data`
                defaultdict to store.
        """
        raise NotImplementedError

    def update_chat_data(self, chat_data):
        """Will be called by the :class:`telegram.ext.Dispatcher` after a handler has
        handled an update. It will be the :attr:`telegram.ext.Dispatcher.chat_data` defaultdict.

        Args:
            chat_data (:obj:`defaultdict`): The :attr:`telegram.ext.dispatcher.chat_data`
                defaultdict to store.
        """
        raise NotImplementedError

    def flush(self):
        """Will be called by :class:`telegram.ext.Updater` upon receiving a stop signal. Gives the
        persistence a chance to finish up saving or close a database connection gracefully. If this
        is not of any importance just pass will be sufficient.
        """
        raise NotImplementedError
