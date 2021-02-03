from Bio import SeqIO
from Bio.Graphics import GenomeDiagram
from reportlab.lib import colors
from reportlab.lib.units import cm

#This program reads the genbank file containing
# the DNA sequence of the Tomato Curly Stunt Virus and
# outputs a circular genome with the features and respective labels.

# The functions to read the genbank file and then draw a diagram
# with the features of the Tomato Curly Stunt Virus.
map1 = SeqIO.read("Genome.gb", "genbank")
gd_diagram = GenomeDiagram.Diagram("Tomato Virus")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

for feature in map1.features:
    if feature.type != "gene":
        continue

    #color coding the features
    if len(gd_feature_set) % 5 == 0:
        color = colors.cyan
    elif len(gd_feature_set) % 5 == 1:
        color = colors.magenta
    elif len(gd_feature_set) % 5 == 2:
        color = colors.greenyellow
    elif len(gd_feature_set) % 5 == 3:
        color = colors.orange
    else:
        color = colors.lightpink
    gd_feature_set.add_feature(feature, color=color, label_position="middle", label=True, label_size=13)

# Establish the dimension of the png file,
# the circle and their respective labels.
gd_diagram.draw(format="circular",circular=True,pagesize=(16*cm,16*cm), start=50, end=len(map1) + 50, circle_core=0.56)
gd_diagram.write("genome_map.png", "PNG")