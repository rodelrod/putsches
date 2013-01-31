===================
Putsches
===================

Project for a web community to debate and intervene on matters of civic interest.

Putsches is based on the code of Askbot, an open source Q&A system created by
Evgeny Fadeev on the basis of CNPROG and OSQA. In fact, at this point Putsches is 
little more than a Askbot fork configured for Heroku deployment. Yet, if you are looking for a Heroku-ready install of Askbot, use the repository https://github.com/rodelrod/askbot-heroku, as the code here will soon diverge from Askbot.

To deploy in heroku:

1. Add the heroku repository as a git remote and push
2. ``syncdb`` and ``migrate``
3. Set environment variables in heroku::
   $ heroku config:set DJANGO_SETTINGS_MODULE=app.settings.prod
   $ heroku config:set SECRET_KEY="some_random_value"

To get a value for SECRET_KEY you can use the linux utility ``apg``.
