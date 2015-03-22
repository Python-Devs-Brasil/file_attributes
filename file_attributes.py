# Description = Some functions to obtain file attributes
# Author = Eduardo Frazão
# Date = 2014/04/25
import os
import time

def fc_time(valor):
    meses = ['', 'Janeiro', 'Feveiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    value = (time.localtime(valor))
    return str(value[2]) + ' de ' + str(meses[value[1]]) + ' de ' + str(value[0]) + ', ' + str(value[3]) + ':' + str(value[4]) + ':' + str(value[5])

def size(file):
    statinfo = os.stat(file)
    bt = statinfo.st_size
    kb = (bt / 1024); mb = (kb / 1024); gb = (mb / 1024)
    if gb >= 1:
        return ('%.1f GB' % gb)
    else:
        if mb >= 1:
            return ('%.1f MB' % mb)
        else:
            if kb >= 1:
                return ('%.1f KB' % kb)
            else:
                return ('%d Bytes' % bt)

def last_access(file):
    global statinfo
    statinfo = os.stat(file)
    return fc_time(statinfo.st_atime)

def last_modification(file):
    global statinfo
    statinfo = os.stat(file)
    return fc_time(statinfo.st_mtime)

def creation(file):
    #creation date in windows environment
    #date of recent metadata change in unix environment
    global statinfo
    statinfo = os.stat(file)
    return fc_time(statinfo.st_ctime)

teste = input('Arquivo:')

print('''\nInformations about: "%s"\n''' % teste)
print('Size:                %s' % str(size(teste)))
print('Created in:          %s' % str(creation(teste)))
print('Last Access:         %s' % str(last_access(teste)))
print('Last Modification:   %s' % str(last_modification(teste)))
