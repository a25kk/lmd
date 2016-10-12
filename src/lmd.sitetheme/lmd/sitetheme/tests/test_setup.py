# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from lmd.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of lmd.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if lmd.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.lmdroductInstalled('lmd.buildout'))

    def test_uninstall(self):
        """Test if lmd.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['lmd.buildout'])
        self.assertFalse(self.installer.lmdroductInstalled('lmd.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IlmdBuildoutLayer is registered."""
        from lmd.buildout.interfaces import IlmdBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IlmdBuildoutLayer in utils.registered_layers())
