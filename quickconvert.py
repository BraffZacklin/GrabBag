#!/bin/env python
import os
from subprocess import call

directory = f'Current Directory: {os.getcwd()}\nDirectory to Access: '
directory = input(directory)
if directory in ['', './']:
	directory = [os.getcwd()]
else:
	directory = [directory]

def cat_files_to_path(files, path):
	all_paths = []
	for f in files:
		all_paths.append(path + '/' + f)
	return all_paths

def file_crawler(directories):
	discovered_files = directories

	for f in directories:
		if os.path.isdir(f) == True:
			discovered_files += cat_files_to_path(os.listdir(f), f)
			discovered_files.remove(f)

	directories_remaining = False
	for f in discovered_files:
		if os.path.isdir(f) == True:
			directories_remaining = True

	if directories_remaining == True:
		return file_crawler(discovered_files)
	else:
		return discovered_files

all_files_full_path = file_crawler(directory)

def filter_to_extless(files):
	extless = []
	for f in files:
		file_name = f.split('/')[-1]
		if '.' not in file_name:
			extless.append(f)
	return extless

extless = filter_to_extless(all_files_full_path)

def make_commands_list(files):
	command_list = []
	for current_filepath in files:
		section = '_000'
		if section in current_filepath:
			final_filepath = replace_in_string(current_filepath, section) + '.png'
		else:
			final_filepath = current_filepath + '.png'
		command_list.append(['sudo', 'mv', current_filepath, final_filepath])
	return command_list

def replace_in_string(string, section, replacement=None):
	old_string = string.split(section)
	if replacement == None:
		if len(old_string) != 1:
			return ''.join(old_string)
	if len(old_string) != 1:
		return old_string[0] + replacement + old_string[-1]
	else:
		if list(section)[-1] == string(string)[-1]:
			return old_string[0] + replacement
		elif list(section)[0] == list(string)[0]:
			return  replacement + old_string[0]

commands = make_commands_list(extless)
for f in commands:
	call(f)