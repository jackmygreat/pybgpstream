#!/usr/bin/env python

from _pybgpstream import BGPStream, BGPRecord, BGPElem

# create a new bgpstream instance
stream = BGPStream()

# create a reusable bgprecord instance
rec = BGPRecord()

# select the datasource interface
stream.set_data_interface('singlefile')

# select the MRT file to be read by the singlefile datasource
stream.set_data_interface_option('singlefile', 'upd-file','./examples/ris.rrc06.updates.1427846400.gz')

# select the time interval to process  Wed Apr  1 00:02:50 UTC 2015 -> Wed Apr  1 00:04:30
stream.add_interval_filter(1427846570, 1427846670)

# start the stream
stream.start()

# print the stream
while(stream.get_next_record(rec)):
    print rec.status, rec.project +"."+ rec.collector, rec.time
    elem = rec.get_next_elem()
    while(elem):
        print "\t", elem.type, elem.peer_address, elem.peer_asn, elem.type, elem.fields
        elem = rec.get_next_elem()
        