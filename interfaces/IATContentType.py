#  ATContentTypes http://sf.net/projects/collective/
#  Archetypes reimplementation of the CMF core types
#  Copyright (c) 2003-2004 AT Content Types development team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA 
#
"""AT Content Types general interface

$Id: IATContentType.py,v 1.5 2004/04/04 21:45:04 tiran Exp $
""" 
__author__  = 'Christian Heimes'
__docformat__ = 'restructuredtext'

from interface import Interface, Attribute

class IATContentType(Interface):
    """Marker interface for AT Content Types
    """

    suppl_views = Attribute('''Supplementary views - used for TemplateMixin''')

    newTypeFor = Attribute('''Used to get the meta type of the original implementation''')

    TypeDescription = Attribute('''A short description used for the edit screen''')

    assocMimetypes = Attribute('''A tuple of mimetypes that are associated
                                  with this type. Format: ('bar/foo', 'foo/*',)
                               ''')

    assocFileExt = Attribute('''A tuple of file extensions that are associated
                                with this type. Format: ('jpeg', 'png',)
                             ''')

    def getLayout(**kw):
        """Get the current layout or the default layout if the current one is None
        """

    def getDefaultLayout():
        """Get the default layout used for TemplateMixin
        """
