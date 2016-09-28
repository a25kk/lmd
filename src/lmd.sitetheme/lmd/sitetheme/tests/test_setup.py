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
        self.assertTrue(self.installer.isProductInstalled('lmd.buildout'))

    def test_uninstall(self):
        """Test if lmd.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['lmd.buildout'])
        self.assertFalse(self.installer.isProductInstalled('lmd.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ILmdBuildoutLayer is registered."""
        from lmd.buildout.interfaces import ILmdBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(ILmdBuildoutLayer in utils.registered_layers())
