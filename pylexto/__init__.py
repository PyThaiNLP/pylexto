﻿# -*- coding: utf-8 -*-
from __future__ import absolute_import,unicode_literals
import pylexto
import jpype
import os

class LexTo (object):
	def __init__(self):
		filePath = os.path.join(os.path.dirname(pylexto.__file__), 'LongLexTo')
		jpype.startJVM(jpype.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (filePath))
		
		LongLexTo = jpype.JClass("LongLexTo")
		self.lexto = LongLexTo('%s/lexitron.txt' % (filePath))
		self.typeString = ["unknown","known","ambiguous","English/Digits","special"]
	def tokenize(self, line):
		line = line.strip()
	
		self.lexto.wordInstance(line)
		typeList = self.lexto.getTypeList()
		typeList = [self.typeString[n.value] for n in typeList]

		wordList = []  
		begin = self.lexto.first()
		while self.lexto.hasNext():
			end = self.lexto.next()
			wordList.append(line[begin:end])
			begin = end

		return wordList, typeList
