# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class AbstractOrganizer:
    """
    Abstract base class for all organizer plugins.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_meta_data(self):
        raise NotImplementedError()


class AbstractSoundOrganizer(AbstractOrganizer):
    """
    Abstract class used for all plugins concerning all sound files.
    """
    __metaclass__ = AbstractOrganizer()

    @abstractmethod
    def get_meta_data(self):
        raise NotImplementedError()


class AbstractImageOrganizer(AbstractOrganizer):
    """
    Abstract class used for all plugins concerning all image files.
    """
    __metaclass__ = AbstractOrganizer()

    @abstractmethod
    def get_meta_data(self):
        raise NotImplementedError()


class AbstractTextFileOrganizer(AbstractOrganizer):
    """
    Abstract class used for all plugins concerning all text files.
    """
    __metaclass__ = AbstractOrganizer()

    @abstractmethod
    def get_meta_data(self):
        raise NotImplementedError()
