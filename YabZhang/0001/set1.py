#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string, random

def generate_codes(len=20):
	return ''.join(random.sample(string.letters+string.digits, len))

file = open("keys.txt", 'w')
for i in range(200):
	code = generate_codes()
	file.write(code[:5]+'-'+code[5:15]+'-'+code[15:] + '\n')

file.close()

