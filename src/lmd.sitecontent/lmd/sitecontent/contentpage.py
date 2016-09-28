# -*- coding: utf-8 -*-
"""Module providing ContentPage content type functionality"""

from plone.dexterity.content import Container
from plone.supermodel import model
from plone.namedfile.interfaces import IImageScaleTraversable
from zope.interface import implelmdter


class IContentPage(model.Schema, IImageScaleTraversable):
    """
    A folderish page
    """


@implelmdter(IContentPage)
class ContentPage(Container):
    pass
