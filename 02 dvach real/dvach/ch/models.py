# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from datetime import datetime

class Post(models.Model):

	txt = models.TextField()
	pub_date = models.DateTimeField(auto_now=datetime.now)
	reply_to = models.ForeignKey("Post", related_name="replies",
									on_delete=models.SET_NULL,
									null=True, blank=True)

	def __unicode__(self):
		return self.txt