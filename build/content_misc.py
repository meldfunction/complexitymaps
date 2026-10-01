"""Orientations, levels of focus, journeys, and braids."""

# Our orientations come from the lineages on this map, each with its source.
ORIENTATIONS = [
    dict(name="Consent before command",
         line="Move when no one has a reasoned objection, rather than waiting for everyone to agree or for someone to order it.",
         source="Sociocracy (Kees Boeke, Gerard Endenburg)",
         ask="Who has not yet been asked whether they can live with this?"),
    dict(name="Match the variety",
         line="A response has to be as varied as the situation it meets. Do not simplify people to fit the system.",
         source="W. Ross Ashby, requisite variety",
         ask="Where are we forcing many different lives through one channel?"),
    dict(name="Widen the choices",
         line="Act so that the people affected have more options afterward, not fewer.",
         source="Heinz von Foerster, the ethical imperative",
         ask="Does this close doors for anyone who was not in the room?"),
    dict(name="Take only what is given",
         line="Relationship before extraction. Ask, take what is offered, share it, and give something back.",
         source="Robin Wall Kimmerer, the Honorable Harvest",
         ask="What are we taking from this community, and what are we returning?"),
    dict(name="Many contexts, no master frame",
         line="Every issue lives in family, work, body, place, and history at once. No single discipline or worldview holds all of it.",
         source="Nora Bateson (transcontextuality), Arturo Escobar (the pluriverse)",
         ask="Which context are we ignoring because it does not fit our frame?"),
    dict(name="Learning over proving",
         line="Treat results as information for the next move, and hold people accountable for learning, not for hitting numbers they do not control.",
         source="Human Learning Systems, developmental evaluation, Deming",
         ask="What did we learn that changes what we do next?"),
    dict(name="Power in plain sight",
         line="Name who decides, whose issues never reach the table, and which beliefs make the arrangement feel natural.",
         source="Steven Lukes, John Gaventa, Paulo Freire",
         ask="Which form of power is doing the work here without being named?"),
]

LEVELS = [
    ("Body and person", "Resmaa Menakem, Staci K. Haines, Robert Kegan, Jennifer Garvey Berger. Practices: somatic work, immunity to change, reflective practice"),
    ("Knowing and perception", "Iain McGilchrist, Evan Thompson, Alicia Juarrero, Terrence Deacon, Isabelle Stengers, Donna Haraway, Karen Barad, Jan Meyer and Ray Land"),
    ("Group and dialogue", "Arawana Hayashi, William Isaacs, Chris Corrigan. Practices: Bohm Dialogue, T-groups, Group Relations, Warm Data Labs, Art of Hosting, Liberating Structures, Work That Reconnects, action learning"),
    ("Organization", "Dave Snowden, Glenda Eoyang, Otto Scharmer, Peter Senge, Amy Edmondson, David Cooperrider, Bjarte Bogsnes, Matthew Skelton and Manuel Pais. Practices: sociocracy, Appreciative Inquiry, Adaptive Action, Beyond Budgeting"),
    ("Community and place", "Nora Bateson, Bayo Akomolafe, adrienne maree brown, Robin Wall Kimmerer, Tyson Yunkaporta, Rebecca Solnit, Daniel Aldrich, Dean Spade. Practices: positive deviance, participatory action research, popular education, mutual aid"),
    ("Society and policy", "Toby Lowe, Geoff Mulgan, Hilary Cottam, Mariana Mazzucato, Jennifer Pahlka, Charles Sabel, Indy Johar, Lou Downe, Michael Quinn Patton, John Gaventa. Practices: Human Learning Systems, developmental evaluation, service design, narrative change"),
    ("Planetary and civilizational", "Vanessa Machado de Oliveira, Jonathan Rowson, Carl Folke, Daniel Christian Wahl, Fritjof Capra, Kate Raworth, Arturo Escobar, Yaneer Bar-Yam"),
]

BRAIDS = [
    ("Nora Bateson + Otto Scharmer", "Relational sensing beside a structured change process. The friction shows what each assumes about intention."),
    ("Bayo Akomolafe + Dave Snowden", "Post-humanist inquiry beside practical sensemaking. Both distrust tidy plans for different reasons."),
    ("Robin Wall Kimmerer + Elinor Ostrom", "Reciprocity beside commons governance. Two routes to the same insight about shared resources."),
    ("Service design + developmental evaluation + transition design", "Journey, learning loop, and long horizon for government innovation."),
    ("Power analysis + Hosting", "Hosting without power analysis can launder existing hierarchies; power analysis without hosting can stay academic."),
    ("Somatic practice + Crisis response", "Regulated bodies make better decisions in the first hours, and recover better afterward."),
]

# Worked journeys use anonymous identifiers.
JOURNEYS = [
    dict(id="quiet-heron", title="From crisis response to city innovation",
         who="quiet-heron started in government crisis response, working with small, ritual-rich communities, and later moved into a city innovation role inside a reluctant bureaucracy.",
         stages=[
             dict(where="Starting point: crisis response in small communities",
                  levels=["Community and place", "Group and dialogue", "Body and person"],
                  pathways=["Crisis", "Ritual", "Somatic", "Indigenous", "Positive deviance"],
                  note="What they already know: communities self-organize in a crisis, ritual holds people through disruption, and regulated bodies make better decisions. These pathways name and deepen that knowledge."),
             dict(where="Arriving in city government",
                  levels=["Organization", "Society and policy"],
                  pathways=["Sensemaking", "Group Relations", "Power analysis", "Government plumbing"],
                  note="Sort ordered from complex problems so procedure can stay procedural. Read resistance as a system defense rather than a personal failing. Learn where procurement, budgets, and audit actually push back."),
             dict(where="Doing the work",
                  levels=["Organization", "Society and policy", "Group and dialogue"],
                  pathways=["Nora Bateson", "Service design", "Developmental evaluation", "Measurement", "Communities of practice"],
                  note="Host Warm Data Labs alongside the structured methods, not upstream of them, to loosen fixed perception. Use service design and developmental evaluation for accountable, learning-based change. Build a community of practice with the people inside who already work this way."),
         ],
         braid="Crisis and ritual knowing carried into the institution: the experience of communities adapting fast is proof of what the bureaucracy could do if its constraints loosened."),
    dict(id="amber-finch", title="From corporate innovation to civic partnerships",
         who="amber-finch ran an innovation team in a large company and now brokers partnerships between business, city government, and community groups.",
         stages=[
             dict(where="Starting point: corporate innovation",
                  levels=["Organization"],
                  pathways=["Corporate innovation", "Strategy under uncertainty", "Teams and learning cultures", "Design thinking"],
                  note="Comfortable with experiments, portfolios, and customer research. Less practiced at working where no one owns the problem."),
             dict(where="Entering civic work",
                  levels=["Community and place", "Society and policy"],
                  pathways=["Collaboration across boundaries", "Power analysis", "Participatory design", "Critical and popular"],
                  note="Learn why design thinking alone can flatten communities into users, and how power shapes who gets to define the problem."),
             dict(where="Doing the work",
                  levels=["Society and policy", "Group and dialogue"],
                  pathways=["Hosting", "Funding and budgeting", "Measurement", "Narrative change"],
                  note="Convene rather than run. Move money toward trust and portfolios, measure learning instead of outputs, and help partners tell a shared story of why change is needed now."),
         ],
         braid="Business speed braided with civic patience: portfolio thinking is an asset in public work once it is paired with shared power."),
]

ABOUT = dict(
    title="Pathways into Complexity",
    lede="Lineages, practices, and methods for working in complex systems, with cases, organizations, and live resources from the Systems Change Learning Guide.",
    worker="https://capacities.jayajohnyramchandani.workers.dev/",
)
