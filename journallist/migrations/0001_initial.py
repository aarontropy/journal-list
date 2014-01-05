# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JLCategory'
        db.create_table(u'journallist_jlcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_text', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'journallist', ['JLCategory'])

        # Adding model 'JLItem'
        db.create_table(u'journallist_jlitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['journallist.JLCategory'])),
            ('item_text', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('pub_date', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'journallist', ['JLItem'])


    def backwards(self, orm):
        # Deleting model 'JLCategory'
        db.delete_table(u'journallist_jlcategory')

        # Deleting model 'JLItem'
        db.delete_table(u'journallist_jlitem')


    models = {
        u'journallist.jlcategory': {
            'Meta': {'object_name': 'JLCategory'},
            'category_text': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'journallist.jlitem': {
            'Meta': {'object_name': 'JLItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['journallist.JLCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_text': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['journallist']