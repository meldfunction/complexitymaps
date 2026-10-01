"""Field Atlas content: the redesign's families, goals, trades, tags, lenses, explainers, and glossary.

Ported from the design handoff (Pathways Redesign.dc.html) on 2026-10-01. Everything here is DRAFT unless marked
otherwise: tags, trades, roles and lenses were written by the design team and still need review against sources.
Pathways are referred to by a short id (SHORT maps it to the real pathway id).
"""

# short id -> pathway id
SHORT = {'cyb': 'cybernetics-the-shared-foundation',
 'cx': 'the-formal-science-of-complex-systems',
 'sense': 'sensemaking-and-acting-in-uncertainty',
 'selforg': 'governance-and-self-organizing-structures',
 'pubpol': 'public-policy-and-government-innovation',
 'sysdes': 'systemic-design-and-futures',
 'econ': 'complexity-economics-and-new-economic-models',
 'strat': 'strategy-under-uncertainty',
 'fund': 'funding-and-budgeting-for-adaptation',
 'meas': 'measurement-and-accountability',
 'plumb': 'government-plumbing',
 'teams': 'teams-and-learning-cultures',
 'corp': 'corporate-innovation-and-renewal',
 'collab': 'collaboration-across-boundaries',
 'reln': 'relational-transcontextual-and-post-humanist-knowing',
 'warm': 'nora-bateson-and-warm-data',
 'indig': 'indigenous-and-land-based-knowledge',
 'theoryu': 'presencing-theory-u-and-social-presencing-theater',
 'meta': 'the-metacrisis-and-meaning',
 'livsys': 'living-systems-and-regeneration',
 'bohm': 'bohm-dialogue',
 'tgroup': 't-groups-and-sensitivity-training',
 'grel': 'group-relations',
 'ai': 'appreciative-inquiry',
 'wtr': 'work-that-reconnects',
 'soma': 'somatic-and-embodied-practice',
 'moves': 'emergence-in-movements-and-social-change',
 'host': 'hosting-and-participatory-practice',
 'power': 'power-analysis',
 'narr': 'narrative-change',
 'conflict': 'conflict-transformation',
 'crisis': 'crisis-disaster-and-high-reliability',
 'ritual': 'ritual-liminality-and-transition',
 'dthink': 'design-thinking',
 'svc': 'service-design',
 'pd': 'participatory-design-and-design-justice',
 'trans': 'transition-design',
 'labs': 'strategic-design-and-policy-labs',
 'improve': 'improvement-and-adaptive-management',
 'deval': 'developmental-evaluation',
 'ar': 'action-research',
 'posdev': 'positive-deviance',
 'exp': 'experiential-learning-and-reflective-practice',
 'transl': 'transformative-learning',
 'popedu': 'critical-and-popular-education',
 'cop': 'communities-of-practice-and-action-learning',
 'adult': 'adult-development-and-immunity-to-change',
 'cxedu': 'complexity-and-education',
 'biosem': 'biosemiotics-and-the-umwelt',
 'semio': 'semiotics-signs-codes-and-meaning-making'}

# four hue families: oklch(0.52 0.09 H)
FAMILIES = {'sci': {'name': 'Science and structure', 'hue': 245},
 'rel': {'name': 'Relational and living', 'hue': 150},
 'chg': {'name': 'Change and power', 'hue': 40},
 'prc': {'name': 'Practice and learning', 'hue': 85}}

CLUSTER_FAMILY = {'Foundations and science': 'sci',
 'Relational, Indigenous, and meaning': 'rel',
 'Living systems': 'rel',
 'Organizing and sensemaking': 'sci',
 'Movements and hosting': 'chg',
 'Living practices': 'rel',
 'Power, narrative, and conflict': 'chg',
 'Crisis and transition': 'chg',
 'Policy, systemic design, and economics': 'sci',
 'Strategy, money, and accountability': 'sci',
 'Design and practice': 'prc',
 'Learning and pedagogy': 'prc'}

# short labels used on maps
SHORT_NAMES = {'cyb': 'Cybernetics',
 'cx': 'Formal complexity science',
 'sense': 'Sensemaking in uncertainty',
 'selforg': 'Self-organizing governance',
 'pubpol': 'Public policy innovation',
 'sysdes': 'Systemic design and futures',
 'econ': 'Complexity economics',
 'strat': 'Strategy under uncertainty',
 'fund': 'Funding for adaptation',
 'meas': 'Measurement and accountability',
 'plumb': 'Government plumbing',
 'teams': 'Teams and learning cultures',
 'corp': 'Corporate innovation',
 'collab': 'Collaboration across boundaries',
 'reln': 'Relational knowing',
 'warm': 'Nora Bateson and Warm Data',
 'indig': 'Indigenous and land-based knowledge',
 'theoryu': 'Presencing and Theory U',
 'meta': 'Metacrisis and meaning',
 'livsys': 'Living systems and regeneration',
 'bohm': 'Bohm Dialogue',
 'tgroup': 'T-groups',
 'grel': 'Group Relations',
 'ai': 'Appreciative Inquiry',
 'wtr': 'Work That Reconnects',
 'soma': 'Somatic practice',
 'moves': 'Emergence in movements',
 'host': 'Hosting',
 'power': 'Power analysis',
 'narr': 'Narrative change',
 'conflict': 'Conflict transformation',
 'crisis': 'Crisis and high reliability',
 'ritual': 'Ritual and liminality',
 'dthink': 'Design thinking',
 'svc': 'Service design',
 'pd': 'Participatory design',
 'trans': 'Transition design',
 'labs': 'Policy labs',
 'improve': 'Improvement and adaptive management',
 'deval': 'Developmental evaluation',
 'ar': 'Action research',
 'posdev': 'Positive deviance',
 'exp': 'Experiential learning',
 'transl': 'Transformative learning',
 'popedu': 'Popular education',
 'cop': 'Communities of practice',
 'adult': 'Adult development',
 'cxedu': 'Complexity and education',
 'biosem': 'Biosemiotics and Umwelt',
 'semio': 'Semiotics'}

# hand-drawn neighbour links for the Universe and Metro maps
EDGES = [('cyb', 'cx'),
 ('cyb', 'selforg'),
 ('cyb', 'sense'),
 ('cx', 'econ'),
 ('sense', 'strat'),
 ('sense', 'crisis'),
 ('sense', 'reln'),
 ('sense', 'grel'),
 ('warm', 'theoryu'),
 ('indig', 'selforg'),
 ('indig', 'livsys'),
 ('svc', 'deval'),
 ('deval', 'trans'),
 ('trans', 'sysdes'),
 ('power', 'host'),
 ('soma', 'crisis'),
 ('crisis', 'ritual'),
 ('posdev', 'crisis'),
 ('pubpol', 'plumb'),
 ('pubpol', 'labs'),
 ('labs', 'svc'),
 ('meas', 'deval'),
 ('cop', 'teams'),
 ('ar', 'popedu'),
 ('exp', 'ar'),
 ('bohm', 'warm'),
 ('bohm', 'host'),
 ('narr', 'moves'),
 ('conflict', 'power'),
 ('plumb', 'sense'),
 ('popedu', 'power'),
 ('theoryu', 'host'),
 ('collab', 'meas'),
 ('ai', 'host'),
 ('strat', 'corp'),
 ('plumb', 'svc'),
 ('biosem', 'livsys'),
 ('biosem', 'semio'),
 ('semio', 'reln'),
 ('semio', 'narr'),
 ('biosem', 'cyb')]

# known trails, drawn as metro lines (fictional composite starting points)
METRO_LINES = [{'id': 'gov',
  'label': 'I work inside government',
  'sub': 'Policy, services, public innovation',
  'trail': ['sense', 'plumb', 'svc', 'deval', 'meas'],
  'why': 'Tell apart problems with known answers from those without, learn where budgets and rules push back, then '
         'find ways to stay accountable while you learn.'},
 {'id': 'host',
  'label': 'I hold groups and conversations',
  'sub': 'Facilitation, dialogue, hosting',
  'trail': ['host', 'bohm', 'warm', 'power', 'theoryu'],
  'why': "Deepen the craft of holding a room, then pair it with power analysis so hosting doesn't launder existing "
         'hierarchies.'},
 {'id': 'org',
  'label': 'I lead a team or organization',
  'sub': 'Strategy, culture, structure',
  'trail': ['strat', 'teams', 'selforg', 'ai', 'meas'],
  'why': "From strategy that expects surprise to structures that share authority, with measurement that doesn't "
         'punish learning.'},
 {'id': 'move',
  'label': 'I organize in community or movements',
  'sub': 'Mutual aid, campaigns, place',
  'trail': ['moves', 'power', 'narr', 'popedu', 'indig'],
  'why': 'Emergent strategy first, then tools to read power and change the stories people act from.'},
 {'id': 'sci',
  'label': 'I want the science underneath',
  'sub': 'Feedback, emergence, networks',
  'trail': ['cyb', 'cx', 'sense', 'econ', 'livsys'],
  'why': 'How the ideas grew: from feedback loops to complexity economics and living systems.'}]

SECTORS = [('gov', 'Government'),
 ('biz', 'Business'),
 ('ngo', 'Nonprofit'),
 ('com', 'Community'),
 ('edu', 'Education and research'),
 ('fund', 'Funding')]

SCALES = [('per', 'Person'),
 ('grp', 'Group'),
 ('org', 'Organization'),
 ('plc', 'Community and place'),
 ('pol', 'Society and policy'),
 ('pla', 'Planetary')]

# DRAFT  short id -> 'sectors|scales'
TAGS = {'cyb': 'edu|org,pol',
 'cx': 'edu|pla,pol',
 'sense': 'gov,biz,ngo|org,pol',
 'selforg': 'biz,ngo,com|org,grp',
 'pubpol': 'gov|pol',
 'sysdes': 'gov,edu|pol,pla',
 'econ': 'edu,gov|pol,pla',
 'strat': 'biz,gov|org',
 'fund': 'fund,gov,ngo|org,pol',
 'meas': 'gov,fund,ngo|org,pol',
 'plumb': 'gov|org,pol',
 'teams': 'biz,gov|grp,org',
 'corp': 'biz|org',
 'collab': 'gov,ngo,fund,com|plc,pol',
 'reln': 'edu,com|per,plc',
 'warm': 'com,ngo,edu|grp,plc',
 'indig': 'com,edu|plc,pla',
 'theoryu': 'biz,gov,ngo|grp,org',
 'meta': 'edu|per,pla',
 'livsys': 'com,edu|plc,pla',
 'bohm': 'ngo,edu|grp',
 'tgroup': 'biz,edu|grp,per',
 'grel': 'biz,gov,ngo|grp,org',
 'ai': 'biz,ngo,gov|org,plc',
 'wtr': 'com|per,grp',
 'soma': 'ngo,com|per',
 'moves': 'com|plc,pol',
 'host': 'ngo,com,gov|grp,plc',
 'power': 'com,ngo,fund|plc,pol',
 'narr': 'com,ngo|pol',
 'conflict': 'com,ngo,gov|grp,plc',
 'crisis': 'gov,com|plc,org',
 'ritual': 'com|per,grp',
 'dthink': 'biz|org',
 'svc': 'gov,biz|org,pol',
 'pd': 'com,ngo|grp,plc',
 'trans': 'edu,gov|pla,pol',
 'labs': 'gov|pol',
 'improve': 'gov,biz|org',
 'deval': 'fund,ngo,gov|org,plc',
 'ar': 'edu,com|grp,plc',
 'posdev': 'com,ngo|plc',
 'exp': 'edu|per,grp',
 'transl': 'edu|per',
 'popedu': 'com,edu|grp,plc',
 'cop': 'gov,ngo,edu|grp,org',
 'adult': 'edu,biz|per',
 'cxedu': 'edu|org,pla',
 'biosem': 'edu,com|plc,pla',
 'semio': 'edu,gov|grp,pol'}

WORK_KINDS = [('sub', 'Subsistence', 'Producing food, shelter and warmth'),
 ('cra', 'Craft', 'Making things with skill and care'),
 ('car', 'Care', 'Tending, raising, supporting others'),
 ('com', 'Communal', 'Labour freely given to and received from community'),
 ('sac', 'Sacred', 'Ceremony, ritual, relationship with meaning'),
 ('int', 'Interior', 'Work on and within the self'),
 ('pol', 'Political', 'Maintaining, contesting, transforming collective structures'),
 ('cre', 'Creative', 'Making culture, meaning, beauty'),
 ('adm', 'Administrative', 'Coordinating collective activity'),
 ('att', 'Attention', 'Where attention itself becomes labour')]

# DRAFT  work kind -> short ids
WORK_TAGS = {'sub': ['livsys', 'indig', 'biosem'],
 'cra': ['dthink', 'svc', 'pd', 'trans', 'improve', 'labs'],
 'car': ['soma', 'crisis', 'posdev', 'wtr', 'adult', 'host'],
 'com': ['selforg', 'moves', 'host', 'collab', 'cop', 'indig', 'ar'],
 'sac': ['ritual', 'meta', 'wtr', 'indig', 'reln'],
 'int': ['soma', 'transl', 'adult', 'theoryu', 'reln', 'meta', 'exp', 'tgroup'],
 'pol': ['power', 'narr', 'conflict', 'moves', 'popedu', 'pubpol', 'grel'],
 'cre': ['narr', 'sysdes', 'trans', 'warm', 'ai', 'semio'],
 'adm': ['plumb', 'meas', 'fund', 'strat', 'sense', 'deval', 'teams', 'corp', 'econ'],
 'att': ['narr', 'cyb', 'warm', 'sense', 'bohm', 'cx', 'semio', 'biosem']}

# DRAFT  home page goals: id, label, examples, short ids
GOALS = [('connect',
  'Understand how things connect',
  'Cybernetics, complexity science, living systems',
  ['cyb', 'cx', 'livsys', 'econ', 'reln', 'cxedu', 'biosem', 'semio']),
 ('uncertain',
  'Decide when things are uncertain',
  'Sensemaking, strategy, crisis response',
  ['sense', 'strat', 'crisis', 'sysdes', 'improve', 'corp']),
 ('others',
  'Work well with others',
  'Dialogue, hosting, Group Relations, conflict',
  ['bohm', 'host', 'grel', 'tgroup', 'conflict', 'ai', 'teams', 'cop', 'selforg']),
 ('policy',
  'Change systems and policy',
  'Public policy, design, funding, measurement',
  ['pubpol', 'plumb', 'labs', 'svc', 'dthink', 'fund', 'meas', 'deval', 'collab']),
 ('power',
  'Build power in communities',
  'Movements, power analysis, narrative, popular education',
  ['moves', 'power', 'narr', 'popedu', 'ar', 'pd']),
 ('grow',
  'Grow as a person',
  'Somatic practice, ritual, adult development',
  ['soma', 'ritual', 'adult', 'transl', 'exp', 'wtr', 'meta', 'theoryu']),
 ('land',
  'Learn from land and tradition',
  'Indigenous and land-based knowledge, regeneration',
  ['indig', 'livsys', 'warm', 'trans', 'posdev', 'biosem'])]

TYPE_LABELS = {'Lineage': ('A lineage', "Thinkers who built on each other's ideas"),
 'Method': ('A method', 'A structured way of doing something'),
 'Practice': ('A practice', 'Something you do regularly, often with others'),
 'Field': ('A field', 'An area of work with its own community'),
 'Structure': ('A structure', 'A way of organizing people or money'),
 'Tradition': ('A tradition', 'Knowledge a people has held over generations'),
 'Hybrid': ('A hybrid', 'A mix of the above')}

SCALE_LABELS = {'per': ('Yourself', 'Body, mind and personal practice'),
 'grp': ('A group', 'Teams, circles, meetings'),
 'org': ('An organization', 'Workplaces, charities, agencies'),
 'plc': ('A place or community', 'Neighbourhoods, towns, regions'),
 'pol': ('A society', 'Policy, law, public systems'),
 'pla': ('The planet', 'Climate, ecology, civilization')}

# DRAFT  id, label, work kinds, scales, a first small step
TRADES = [('teach',
  'Teaching and training',
  ['car', 'int', 'com'],
  ['grp', 'per'],
  'Try a new activity with one class before changing the whole course.'),
 ('care', 'Nursing, health and care', ['car'], ['per', 'grp'], 'Try a new handover routine on one shift first.'),
 ('build',
  'Building and trades',
  ['cra', 'adm'],
  ['org', 'plc'],
  'Test a new method on one small job before the big one.'),
 ('food',
  'Farming, food and land',
  ['sub', 'com'],
  ['plc', 'pla'],
  'Trial a new planting in one bed, not the whole field.'),
 ('make', 'Design and making', ['cra', 'cre'], ['grp', 'org'], 'Make a rough version and watch someone use it.'),
 ('office', 'Office, admin and operations', ['adm'], ['org'], 'Change one form for one month and see what happens.'),
 ('lead', 'Managing people', ['adm', 'int'], ['grp', 'org'], 'Let one team try a new way of meeting for a month.'),
 ('policy',
  'Policy and public service',
  ['adm', 'pol'],
  ['pol', 'org'],
  'Try a rule change in one area first, with a clear way to stop.'),
 ('organize',
  'Organizing and advocacy',
  ['pol', 'com'],
  ['plc', 'pol'],
  'Try a new message on one street before the whole campaign.'),
 ('arts',
  'Arts, media and storytelling',
  ['cre', 'att'],
  ['grp', 'pol'],
  'Share a rough cut with a small audience first.'),
 ('research',
  'Research and analysis',
  ['att', 'adm'],
  ['org', 'pla'],
  'Run a small study before committing to the big one.'),
 ('tech', 'Tech and data', ['cra', 'att'], ['org'], 'Release to a few users and watch before rolling out.'),
 ('home',
  'Caring at home',
  ['car', 'com'],
  ['per', 'plc'],
  'Try a new routine for a week and see how everyone feels.'),
 ('faith',
  'Faith, ceremony and community life',
  ['sac', 'com'],
  ['grp', 'plc'],
  'Try a new kind of gathering once before making it regular.'),
 ('between',
  'Studying, retired or between things',
  ['int'],
  ['per'],
  'Try one new thing for a week and notice what changes.')]

INDUSTRIES = [('govt', 'Government', ['gov']),
 ('health', 'Health', ['gov', 'ngo']),
 ('edu', 'Schools and universities', ['edu']),
 ('biz', 'Business', ['biz']),
 ('ngo', 'Charity and nonprofit', ['ngo']),
 ('hood', 'Neighbourhood and community', ['com']),
 ('land', 'Land and environment', ['com', 'edu']),
 ('culture', 'Arts and culture', ['com', 'ngo']),
 ('fund', 'Funding and philanthropy', ['fund']),
 ('none', 'No single place', [])]

# DRAFT  example roles per trade
ROLES = {'teach': ['Teacher', 'Trainer or coach', 'Youth worker', 'Adult education volunteer'],
 'care': ['Nurse', 'Care coordinator', 'Peer support worker', 'Hospice volunteer'],
 'build': ['Site manager', 'Tradesperson', 'Repair café volunteer', 'Housing co-op member'],
 'food': ['Grower', 'Food hub coordinator', 'Community garden organizer', 'Land steward'],
 'make': ['Designer', 'Service designer', 'Makerspace volunteer', 'Product manager'],
 'office': ['Operations lead', 'Programme manager', 'Board secretary (volunteer)', 'Policy officer'],
 'lead': ['Team lead', 'Director', 'Committee chair', 'Facilitator'],
 'policy': ['Policy advisor', 'Public servant', 'Local councillor', "Citizens' assembly member"],
 'organize': ['Community organizer', 'Campaigner', "Tenants' union rep", 'Mutual aid coordinator'],
 'arts': ['Artist', 'Journalist', 'Community storyteller', 'Podcast producer'],
 'research': ['Researcher', 'Evaluator', 'Data analyst', 'Citizen scientist'],
 'tech': ['Developer', 'Data scientist', 'Civic tech volunteer', 'Digital service lead'],
 'home': ['Family carer', 'Neighbourhood rep', 'School governor', 'Parent group organizer'],
 'faith': ['Faith leader', 'Chaplain', 'Ceremony holder', 'Community elder'],
 'between': ['Volunteer', 'Student', 'Mentor', 'Apprentice']}

# areas of work on the learning tree
BRANCHES = [('care', 'Caring and teaching', ['care', 'teach', 'home']),
 ('make', 'Making and building', ['build', 'make', 'tech']),
 ('land', 'Land and food', ['food']),
 ('public', 'Organizing and public life', ['organize', 'policy']),
 ('run', 'Running things', ['office', 'lead', 'research']),
 ('meaning', 'Culture and meaning', ['arts', 'faith']),
 ('open', 'Figuring it out', ['between'])]

AREA_LENS = {'care': 'Every person, family and class is different, and what works depends on the relationship.',
 'make': 'Whatever you make meets real use, and people do things with it you never planned for.',
 'land': 'Soil, weather, plants and people shape each other over seasons and generations.',
 'public': "Many interests pull at once. No one controls the outcome, and power shapes what's possible.",
 'run': 'Plans meet reality: budgets, rules and people interact in ways no org chart shows.',
 'meaning': 'Stories, rituals and art shape how people see the world, and so how they act in it.',
 'open': "Not knowing what's next is uncertain, but it's also room to explore."}

# cluster-level fallback lens (regex on cluster name)
CLUSTER_LENS = [('Foundations',
  'Complexity as many interacting parts producing patterns no single part explains, with feedback loops that make '
  'the whole steer itself.'),
 ('Organizing',
  'Complexity as a kind of situation: one where cause and effect only make sense looking back, so you probe, sense '
  'and respond.'),
 ('Relational',
  'Complexity as relationship: nothing exists on its own, and understanding comes from the connections between '
  'things, including us.'),
 ('Movements',
  'Complexity as emergence: small, local actions and relationships add up to large change nobody planned centrally.'),
 ('Living systems',
  'Complexity as life itself: self-making networks that keep renewing themselves and their surroundings.'),
 ('Power',
  "Complexity as power and story: what's visible, hidden and taken for granted shapes what people believe is "
  'possible.'),
 ('Crisis',
  'Complexity as disruption: sudden change exposes how fragile or adaptive a system is, and thresholds matter.'),
 ('Policy',
  'Complexity as wicked problems: issues with no final definition, no single owner, and no solution that stays '
  'solved.'),
 ('Living practices',
  'Complexity lived in the room and the body: groups and people carry patterns below awareness that shape what '
  'happens.'),
 ('Strategy',
  'Complexity as the gap between plan and reality: strategy, money and measures have to adapt as things unfold.'),
 ('Design',
  'Complexity as the mess designs have to work in: understand by making, testing and learning with the people '
  'involved.'),
 ('Learning',
  'Complexity of mind: how people grow in their capacity to hold many views, uncertainty and contradiction.')]

# DRAFT  pathway-specific lens; check against sources
PATH_LENS = {'cybernetics-the-shared-foundation': "Complexity as variety. Ashby's law says anything that steers a system must be "
                                      'able to match the variety of what it faces. Later cyberneticians added that '
                                      'the observer is part of the system.',
 'sensemaking-and-acting-in-uncertainty': 'Complexity as a domain. In Cynefin, a complex situation is one where '
                                          'cause and effect can only be seen in hindsight, so you run small probes, '
                                          'sense what happens and respond, rather than analyse and plan.',
 'the-formal-science-of-complex-systems': 'Complexity as many agents following simple local rules, producing '
                                          'emergent, non-linear behaviour that can be modelled but rarely predicted '
                                          'precisely.',
 'power-analysis': 'Complexity as layered power: visible decisions, hidden agenda-setting, and invisible norms, '
                   'operating at different levels and in different spaces.',
 'emergence-in-movements-and-social-change': 'Complexity as emergence: patterns at scale grow from small, repeated '
                                             'relationships and practices, so how you work locally is the strategy.',
 'crisis-disaster-and-high-reliability': 'Complexity as the unexpected: high-reliability organizations stay alert to '
                                         'small failures and defer to whoever has the most relevant expertise in the '
                                         'moment.',
 'complexity-economics-and-new-economic-models': 'Complexity as an economy that is always forming: agents adapt to '
                                                 'patterns they create together, so markets rarely settle into '
                                                 'equilibrium.'}

# DRAFT  two plain paragraphs for 'What it is'
EXPLAINERS = {'sensemaking-and-acting-in-uncertainty': ["Sensemaking is how people work out what's going on when a situation is "
                                           'unclear, before deciding what to do. This pathway gathers practical '
                                           'tools for it. The best known is Cynefin, which sorts situations by how '
                                           'well cause and effect can be known: clear, complicated, complex or '
                                           'chaotic.',
                                           'In clear and complicated situations you can analyse and plan. In complex '
                                           'ones, cause and effect only make sense looking back, so you act in '
                                           'small, reversible steps, watch what happens and adjust. Many '
                                           'organizations get into trouble by treating complex problems as if they '
                                           'had a knowable answer.'],
 'cybernetics-the-shared-foundation': ['Cybernetics studies how systems steer themselves using feedback: a '
                                       'thermostat, a body keeping its temperature, a team adjusting after a result. '
                                       'Its founders in the 1940s and 50s saw the same patterns in machines, brains '
                                       'and societies.',
                                       'A later branch, second-order cybernetics, added that the observer is part of '
                                       'the system being observed, so how you look shapes what you find. Much of the '
                                       'rest of this map grows from these ideas.']}

# DRAFT  plain rewrites of overview (ov) and policy (pol)
PLAIN = {'sensemaking-and-acting-in-uncertainty': {'ov': "Tools for working out what's going on when nobody can know the "
                                                 'answer in advance, and acting in small steps.',
                                           'pol': 'Used in government to plan for risk, run small tests instead of '
                                                  "big pilots, and treat people's own stories as up-to-date "
                                                  'evidence.'},
 'cybernetics-the-shared-foundation': {'ov': 'How systems steer themselves through feedback, and why the observer is '
                                             'part of the picture.'}}

# DRAFT  term -> plain definition
GLOSSARY = {'cynefin': 'A framework from Dave Snowden that sorts situations into clear, complicated, complex and chaotic. Each '
            'needs a different way of acting.',
 'sensemaking': "Working out together what's going on in an unclear situation, before deciding what to do.",
 'feedback': 'When the result of an action loops back and shapes the next action.',
 'requisite variety': "Ashby's law: to steer something, your responses need to be at least as varied as the "
                      'situations you face.',
 'cybernetic': 'About steering through feedback, in machines, living things or organizations.',
 'safe-to-fail': 'A small experiment designed so that if it fails, the damage is small and you still learn.',
 'emergence': 'When a whole shows patterns that none of its parts have on their own.',
 'service design': 'Designing a service end to end: what people experience and the behind-the-scenes work that makes '
                   'it happen.',
 'service blueprint': 'A diagram of a service showing what users see, and the backstage work behind each step.',
 'journey map': 'A picture of the steps someone goes through to get something done, and how each step feels.',
 'good services': "Lou Downe's plain-language standards for what makes a service work well for the people using it.",
 'user research': 'Learning directly from the people who use a service: watching, asking, testing.'}

