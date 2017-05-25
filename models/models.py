# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
from datetime import datetime, timedelta


class CourseExtension(models.Model):
    _inherit = 'openacademy.course'

    def _start_date(self):
        for record in self:
            record.end_date = fields.Datetime.from_string(record.start_date)
    # ampliacion ernesto: numero de sesiones y dias para todas las semanas generar las sesiones
    start_date = fields.Date(default=fields.Date.today)
    number_sessions = fields.Integer(string="Number of sessions", required=True)
    end_date = fields.Date(default=_start_date)
    today = fields.Date(default=fields.Date.today)
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

    @api.onchange('session_id')
    def calculate_end_date(self):
        import pdb; pdb.set_trace()
        self.end_date = self.end_date - timedelta(years=100)
        for sess in self.session_ids:
            # if fields.Datetime.from_string(sess.end_date) > fields.Datetime.from_string(self.end_date):
            if sess.end_date > self.end_date:
                self.end_date = fields.Datetime.from_string(sess.end_date)

    @api.depends('datetime.date.today()')
    def _update_today(self):
        today = datetime.date.today()

    @api.multi
    def action_created(self):
        self.state = 'created'

    @api.multi
    def action_subscribing(self):
        self.state = 'subscribing'

    @api.multi
    def action_closed(self):
        self.state = 'closed'

    @api.multi
    def action_started(self):
        self.state = 'started'

    @api.multi
    def action_finished(self):
        self.state = 'finished'
