from fhrs_osm import *
import config

db = Database(config.dbname)
db.connect()

# compute districts
print "Adding district ID for FHRS establishments"
db.add_fhrs_districts()
print "Adding district ID for OSM entities"
db.add_osm_districts()

# create database views
print "Creating database view for data comparison"
db.create_comparison_view()
print "Creating database view to suggest FHRS/OSM matches"
db.create_suggest_matches_view()
print "Creating database view for distant matches"
db.create_distant_matches_view(distance_metres=config.warning_distance_metres)
