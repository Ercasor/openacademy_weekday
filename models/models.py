# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
from datetime import datetime, timedelta


class CourseExtension(models.Model):
    _inherit = 'openacademy.course'

    # ampliacion ernesto: numero de sesiones y dias para todas las semanas generar las sesiones
    start_date = fields.Date(default=fields.Date.today)
    number_sessions = fields.Integer(string="Number of sessions", required=True)
    week_days = fields.Selection([('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], "Weekly Holiday")
    state = fields.Selection([('created', "Created"), ('subscribing', "Subscribing"), ('closed', "Closed"), ('started', "Started"), ('finish', "Finished")], default='created')

    @api.one
    def generate_sessions(self):
        if len(self.session_ids) > 0:
            # import pdb; pdb.set_trace()
            raise exceptions.Warning('Actual Course has some sessions created previously. Check and delete them manually')
            # raise exceptions.except_orm(('Course has sessions'),
            #      ('Actual Course has some sessions created previously. Check and delete them manually'),)

        else:
            for num in range(0, self.number_sessions):
                day = fields.Datetime.from_string(self.start_date) + timedelta(days=(num*7))
                session_name = str(self.name + '-session' + str(num))
                session = self.env['openacademy.session'].create({'name': session_name, 'course_id': self.id, 'active': True, 'start_date': day})
                self.write({'session_ids': [(4, session.id)]})
