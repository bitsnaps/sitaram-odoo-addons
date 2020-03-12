# -*- coding: utf-8 -*-
#############################################################################################
#                                                                                           #
#    Maurya Software Solutions                                                              #
#    Copyright (C) 2018-TODAY freepros.                                                     #
#    Author: freepro                                                                        #
#    you can modify it under the terms of the GNU LESSER                                    #
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.                                           #
#                                                                                           #
#    It is forbidden to publish, distribute, sublicense, or sell copies                     #
#    of the Software or modified copies of the Software.                                    #
#                                                                                           #
#    This program is distributed in the hope that it will be useful,                        #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                         #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                          #
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.                          #
#                                                                                           #
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE               #
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.                              #
#    If not, see <http://www.gnu.org/licenses/>.                                            #
#                                                                                           #
#############################################################################################

{

    "name" : "Client Fournisseur Master",
    "version" : "1.0",
    "author" : "Free pro Software Solutions",
    "description": """Showing customer supplier template as a master
    """,
    'website': 'www.freepro.com',
    'category': 'partner',
    'depends': ['base','account_invoice_due_mac5','account_payment_group'],
    'data': [
        'views/mss_partner_view.xml',
    ],
    'demo': [
    ],

    'images': ['static/description/partner_banner.png'],
    "application":  True,
    "installable":  True,
    "auto_install":  False,
    'license': 'AGPL-3',
}


