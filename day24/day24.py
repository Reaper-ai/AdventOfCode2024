import re
from pyvis.network import Network
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import networkx as nx
import dash
import dash_cytoscape as cyto
from dash import html



WIRES, ops = open("input").read().split("\n\n")

WIRES = dict([i.split(": ") for i in WIRES.split("\n")])
for i in WIRES:
    WIRES[i] = int(WIRES[i])

ops = [re.findall(r"\w{3}|OR", i) for i in ops.split("\n")]
all_wires = set()
for i,j,k,l in ops:
    all_wires.add(i)
    all_wires.add(k)
    all_wires.add(l)
###########################################################################################
# part 2 manual swap check
#--------------------------------------------------------------------------------------
change = dict()
for i in range(len(ops)):
    a ,b ,c, d = ops[i]

    if d in ["z38","qrh","gmh","z13","jmq","z06","cbd","rqf"]:
        change[d] = i

print(change)
ops[change["z38"]][3], ops[change["qrh"]][3] = ops[change["qrh"]][3], ops[change["z38"]][3]
ops[change["gmh"]][3],ops[change["z13"]][3] = ops[change["z13"]][3], ops[change["gmh"]][3]
ops[change["jmq"]][3],ops[change["z06"]][3] = ops[change["z06"]][3], ops[change["jmq"]][3]
ops[change["cbd"]][3],ops[change["rqf"]][3] = ops[change["rqf"]][3], ops[change["cbd"]][3]
#__________________________________________________________________________________________
###########################################################################################
def part_1(ops = ops):
    wires = dict(WIRES)
    for wire in all_wires:
        if wire not in wires:
            wires[wire] = None

    def flag(): return any(map(lambda x: x is None, list(wires.values())))

    while flag():
        for in1, gate, in2, out in ops:
            if wires[in1] is None or wires[in2] is None:
                continue

            else:
                if gate == "AND":
                    wires[out] = wires[in1] & wires[in2]
                elif gate == "OR":
                    wires[out] = wires[in1] | wires[in2]
                elif gate == "XOR":
                    wires[out] = wires[in1] ^ wires[in2]

    return wires
def find_num(wires,c):
    res = []
    for wire in wires:
        if wire[0] == c:

            res.append((wire, wires[wire]))

    result = int("".join([str(i[1]) for i in list(reversed(sorted(res, key=lambda x: x[0])))]), 2)
    return result
wires = part_1()
result = find_num(wires,"z")
print("result part 1", result)
# for part 2
int1 = find_num(WIRES,"x")
int2 = find_num(WIRES,"y")
expected = int1 + int2
print(bin(expected^result))

#part 2 ###################################################################
print(*sorted(["z38","qrh","gmh","z13","jmq","z06","cbd","rqf"]),sep=",")
##########################################################################



# graphing to visually find swapped nodes
####################################################################################
'''
a = iter(range(500))
o = iter(range(500))
x = iter(range(500))

G = nx.DiGraph()
ins = set()
outs = set()
inter =set()
gt1 = []
gt2 = []
gt3 = []
edges = []

for in1, gate, in2, out in ops:
    if gate == "AND":
        gat = "AND"+str(next(a))
    elif gate == "OR":
        gat ="OR"+str(next(o))
    elif gate == "XOR":
        gat = "XOR"+str(next(x))

    if gat[0] == "A" and (in1[0] in "xy" or in2[0] in "xy"):
        gt2.append(gat)
    elif gat[0] == "X" and (in1[0] in "xy" and in2[0] in "xy"):
        gt1.append(gat)
    elif gat[0] == "X" and out[0] == "z":
        gt2.append(gat)
    elif gat[0] == "O":
        gt3.append(gat)
    else:
        gt2.append(gat)

    if in1[0] in "xy":
        ins.add(in1)
    else:
        inter.add(in1)
    if in2[0] in "xy":
        ins.add(in2)
    else:
        inter.add(in2)

    if out[0] == "z":
        outs.add(out)
    else:
        inter.add(out)

    edges.extend([[in1,gat],[in2,gat],[gat,out]])

G.add_nodes_from(list(inter)+list(ins)+list(outs)+gt1+gt2+gt3)
G.add_edges_from(edges)
plt.figure(figsize=(12, 8))
pos = nx.kamada_kawai_layout(G)


'''

"""

#____________________________________________________________________________________________________________________
app = dash.Dash(__name__)

# Define Cytoscape elements
elements = []
for node, position in pos.items():
    elements.append({
        'data': {'id': node, 'label': node},
        'position': {'x': position[0] * 5000, 'y': position[1] * 5000},
        'grabbable': True
    })

for edge in G.edges():
    elements.append({
        'data': {'source': edge[0], 'target': edge[1]}
    })

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape',
        elements=elements,
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '750px','background-color':'black'},
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'content': 'data(label)',
                    'text-valign': 'center',
                    'color': 'white',
                    'background-color': '#0074D9',
                    'width':30,
                    'height':20,
                    'font_size': '12px'

                }
            },
            {
                'selector': 'edge',
                'style': {
                    'line-color': '#888',
                    'target-arrow-color': '#888',
                    'target-arrow-shape': 'vee',
                    'curve-style': 'bezier',
                    'arrow-scale': 1.5
                }
            },
            {
                'selector': ':selected',
                'style': {
                    'background-color': '#FF4136',
                    'line-color': '#FF4136'
                }
            }
        ]
    )
])




if __name__ == '__main__':
    app.run_server(debug=True)

"""
""""
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0 * 1000)
    edge_x.append(x1 * 1000)
    edge_x.append(None)
    edge_y.append(y0 * 1000)
    edge_y.append(y1 * 1000)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x,
    y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')


node_x = []
node_y = []
node_text = []

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x * 1000)
    node_y.append(y * 1000)
    node_text.append(node)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=node_text,
    textposition='top center',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

# Build the Plotly figure
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='Interactive 45-bit Binary Adder Schematic',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20, l=5, r=5, t=40),
                    annotations=[dict(
                        text="",
                        showarrow=False,
                        xref="paper", yref="paper")],
                    xaxis=dict(showgrid=False, zeroline=False),
                    yaxis=dict(showgrid=False, zeroline=False))
                )

fig.show()

""""""
net = Network(height='750px', width='100%', directed=True)
# Add nodes and edges from NetworkX graph to PyVis network net.from_nx(G) # Set the initial positions
for node, (x, y) in pos.items():
    net.nodes.append({'id': node, 'x': x * 1000, 'y': y * 1000})

net.repulsion(node_distance=200, spring_length=200)
net.show('interactive_graph_with_initial_positions.html')
""""""
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=200, edge_color='gray', arrowsize=10, font_size=10)
# Draw the edges with arrows
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowstyle='->', arrowsize=20)

# Display the graph
plt.show()
"""