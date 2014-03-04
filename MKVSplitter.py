import subprocess
import xml.etree.ElementTree as ET

filename = input('Please input your MKV filename: ')

xmlname = 'chap_info.xml'
filename = '"%s"' % filename
command = 'ffprobe -show_chapters -i %s -print_format xml > %s' % (filename, xmlname)

subprocess.call(command, shell=True)

tree = ET.parse(xmlname)
root = tree.getroot()[0]

debug = False

for chap in root:
    st = chap.attrib['start_time']
    ed = chap.attrib['end_time']
    tt = chap[0].attrib['value']
    outname = '"%s.mkv"' % tt
    command = 'ffmpeg -i %s -vcodec copy -acodec copy -map 0 -sn -ss %s -to %s %s' % (filename, st, ed, outname)
    print(command)
    subprocess.call(command)
    if debug:
        break

print('DONE')
