##############################################################################
#
# Copyright (c) 2001 Zope Corporation and Contributors. All Rights Reserved.
# Copyright (c) 2002 Ingeniweb SARL
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################

"""GroupUserFolder product"""

from Globals import MessageDialog, DTMLFile      # fakes a method from a DTML file
from AccessControl import ClassSecurityInfo
from Globals import InitializeClass
from Acquisition import Implicit
from Globals import Persistent
from AccessControl.Role import RoleManager
from OFS.SimpleItem import Item
from OFS.PropertyManager import PropertyManager
import OFS
from OFS import ObjectManager, SimpleItem
from DateTime import DateTime
from App import ImageFile
import DynaList
import AccessControl.Role, webdav.Collection
import Products
import os
import string
import shutil
import random


##def dummy_add():
##    """ """
##    return None



def manage_addGRUFUsers(self,dtself=None,REQUEST=None,**ignored):
    """ """
    f=GRUFUsers()
    self=self.this()
    try:    self._setObject('Users', f)
    except: return MessageDialog(
                   title  ='Item Exists',
                   message='This object already contains a GRUFUsers Folder',
                   action ='%s/manage_main' % REQUEST['URL1'])
    self.Users._post_init()
    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect(self.absolute_url()+'/manage_main')



def manage_addGRUFGroups(self,dtself=None,REQUEST=None,**ignored):
    """ """
    f=GRUFGroups()
    self=self.this()
    try:    self._setObject('Groups', f)
    except: return MessageDialog(
                   title  ='Item Exists',
                   message='This object already contains a GRUFGroups Folder',
                   action ='%s/manage_main' % REQUEST['URL1'])
    self.Groups._post_init()
    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect(self.absolute_url()+'/manage_main')



class GRUFFolder(OFS.ObjectManager.ObjectManager, OFS.SimpleItem.Item, ):
    isAnObjectManager=1
    isPrincipiaFolderish=1
    manage_main=DTMLFile('dtml/GRUFFolder_main', globals())
    manage_options=(
        {'label':'Contents', 'action':'manage_main',
         },
        ) + OFS.SimpleItem.Item.manage_options


    def header_text(self,):
        """
        header_text(self,) => Text that appears in the content's view heading zone
        """
        return ""


    def getUserFolder(self,):
        """
        getUserFolder(self,) => get the underlying user folder, UNRESTRICTED !
        """
        if not "acl_users" in self.objectIds():
            raise "ValueError", "Please put an acl_users in %s before using GRUF" % (self.getId(),)
        return self.acl_users
        


class GRUFUsers(GRUFFolder):            #, RoleManager):
    """
    GRUFUsers : GRUFFolder that holds users
    """
    meta_type="GRUFUsers"
    id = "Users"

    manage_options = GRUFFolder.manage_options


    class C__ac_roles__(Persistent, Implicit, DynaList.DynaList):
        """
        __ac_roles__ dynastring.
        Do not forget to set _target to class instance.
        """
        def data(self,):
            return self.userdefined_roles()


    ac_roles = C__ac_roles__()
    __ac_roles__ = ac_roles


    def _post_init(self,):
        self.id = "Users"


    def header_text(self,):
        """
        header_text(self,) => Text that appears in the content's view heading zone
        """
        if not "acl_users" in self.objectIds():
            return "Please put an acl_users here before ever starting to use this object."

        ret = """In this folder, groups are seen as ROLES from user's view. To put a user into a group, affect him a role that matches his group.<br />"""

        self.__ac_roles__._target = self
        return ret


    def listGroups(self,):
        """
        listGroups(self,) => return a list of groups defined as roles
        """
        return self.Groups.listGroups()


    def userdefined_roles(self):
        "Return list of user-defined roles"
        return self.listGroups()





class GRUFGroups(GRUFFolder):
    """
    GRUFGroups : GRUFFolder that holds groups
    """
    meta_type="GRUFGroups"
    id = "Groups"

    _group_prefix = "group_"

    def _post_init(self,):
        self.id = "Groups"


    def header_text(self,):
        """
        header_text(self,) => Text that appears in the content's view heading zone
        """
	ret = ""
        if not "acl_users" in self.objectIds():
            return "Please put an acl_users here before ever starting to use this object."

        # Show groups
        return ret
        

    def listGroups(self, without_prefix = 0):
        """
        Return a list of available groups.
        Group names are prefixed !
        """
        if without_prefix:
            return self.acl_users.getUserNames()
        else:    
            return map(lambda x, self=self: "%s%s" % (self._group_prefix, x), self.acl_users.getUserNames())


   
InitializeClass(GRUFUsers) 
InitializeClass(GRUFGroups) 



