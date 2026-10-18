{
    "name": "Respect Theme",
    "version": "19.0.1.0.0",
    "depends": ["web"],
    "license": "LGPL-3",
    "installable": True,
    "assets": {
        "web._assets_primary_variables": [
            ("before","web/static/src/scss/primary_variables.scss","respect_theme/static/src/scss/primary_variables.scss")
        ]
    },
    "data":[
        "views/webclient_templates.xml"
    ]
}