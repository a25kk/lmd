# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from lmd.sitecontent.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of lmd.sitecontent into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if lmd.sitecontent is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.lmdroductInstalled('lmd.sitecontent'))

    def test_uninstall(self):
        """Test if lmd.sitecontent is cleanly uninstalled."""
        self.installer.uninstallProducts(['lmd.sitecontent'])
        self.assertFalse(self.installer.lmdroductInstalled('lmd.sitecontent'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ILmdSitecontentLayer is registered."""
        from lmd.sitecontent.interfaces import ILmdSitecontentLayer
        from plone.browserlayer import utils
        self.failUnless(ILmdSitecontentLayer in utils.registered_layers())
