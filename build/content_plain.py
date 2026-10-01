"""Plain-English one-line overviews (ov) and government/policy notes (pol) for each pathway, keyed by short id.

These replace the longer, more technical overview and policy text wherever the app shows a summary (wiki article
lede, cards, map side panels). Written 2026-10-01 from each pathway's own content; DRAFT until checked.
content_atlas.PLAIN wins where both exist. Where a pathway has no entry here, the original text is shown.
"""

OV = {'adult': 'How adults grow in their capacity to hold complexity, and why people stay stuck even when they want to '
          'change.',
 'ai': 'Change that starts from what already works: asking people about their best experiences, imagining more of '
       'them, and designing from there.',
 'ar': 'Research done with people, not on them: participants study their own situation and act on what they learn, '
       'in cycles.',
 'biosem': 'The study of how living things make and read signs, from cells to forests, and why meaning is part of '
           'life itself.',
 'bohm': 'A way for groups to think together by noticing their assumptions as they speak, with no decision on the '
         'table.',
 'collab': 'How many organizations work together on one shared problem when no single one owns it.',
 'conflict': 'Treating conflict as information about a system and a chance to change relationships, not just a '
             'problem to settle.',
 'cop': 'Learning held by groups of practitioners over time: communities of practice share a field, and action '
        'learning sets work on real problems through questions.',
 'corp': 'How established organizations explore new value while running the current business, and when they need to '
         'break into smaller self-managing units.',
 'crisis': 'What people and organizations do when normal order breaks, and how high-risk organizations stay alert to '
           'small failures.',
 'cx': 'The science of how many simple parts, each following local rules, produce patterns nobody designed: flocks, '
       'traffic, markets, epidemics.',
 'cxedu': 'Seeing classrooms and schools as complex systems, and asking how to educate people for a world nobody can '
          'predict.',
 'deval': 'Evaluation that supports innovation in complex settings: an evaluator works alongside the team, feeding '
          'back what is emerging so the work can adapt.',
 'dthink': "A human-centred way of solving problems: understand people's needs, generate ideas, and test rough "
           'prototypes quickly.',
 'econ': 'Economics that treats the economy as a complex, changing system inside society and nature, rather than a '
         'machine that settles at equilibrium.',
 'exp': 'Learning as a cycle of doing, noticing, making sense and trying again: the base layer for learning '
        'complexity.',
 'fund': 'Money that can follow learning: rolling budgets, portfolios of experiments, and funders who trust the '
         'people they fund.',
 'grel': 'A way of studying authority, leadership and the hidden emotional life of groups by experiencing them '
         'directly, developed at the Tavistock Institute.',
 'host': 'Ways of hosting conversations that matter, so that many voices shape the outcome: Art of Hosting, Open '
         'Space, World Café, Liberating Structures.',
 'improve': 'Getting better through small, repeated cycles: plan, do, study, act, with the people who do the work.',
 'indig': 'Ways of knowing held by Indigenous peoples and land-based communities, where knowledge comes from long '
          'relationship with a place and carries obligations.',
 'labs': 'Teams inside or alongside government that use design and experimentation to make policy, from the UK '
         'Policy Lab to Helsinki Design Lab.',
 'livsys': 'Seeing organizations, cities, and economies as living systems that renew themselves, and designing so '
           'they regenerate rather than deplete.',
 'meas': 'Why targets distort what they measure, and how to be accountable when outcomes are emergent.',
 'meta': "The idea that today's crises in climate, politics, technology and meaning are linked, with a shared root "
         'in how we think and what we value.',
 'moves': 'How large social change grows from small, local relationships and practices, and how movements organize '
          'without central control.',
 'narr': 'Changing the deep stories a society uses to make sense of an issue, so different choices become thinkable.',
 'pd': 'Design with, not for: the people affected by a design take part in making it, and design is used to shift '
       'power toward communities.',
 'plumb': 'The rules, contracts and routines where bureaucracies actually resist change: procurement, regulation, '
          'budgets and frontline discretion.',
 'popedu': 'Education as a practice of freedom: learners read their own world, name what shapes it, and act '
           'together.',
 'posdev': 'Finding people who already succeed against the odds with the same resources as everyone else, and '
           'helping others learn their practices.',
 'power': 'Tools for seeing power: who decides, whose issues never reach the table, and which beliefs make an '
          'arrangement feel natural.',
 'pubpol': 'How governments are learning to work on problems that do not stay solved, through public innovation, '
           'missions and learning-based management.',
 'reln': 'A family of thinkers who start from relationships rather than separate things, and question the idea that '
         'humans stand apart from the world.',
 'ritual': 'Why ritual matters in change: transitions pass through a threshold where old roles end before new ones '
           'begin, and communities have long held people through that in-between.',
 'selforg': 'Ways of sharing authority: sociocracy, holacracy, commons governance and other structures where '
            'decisions are made close to the work, by consent.',
 'semio': 'The study of signs: how words, images, symbols and objects come to mean something, and how cultures make '
          'some meanings seem natural.',
 'soma': 'Change that lives in the body: how bodies hold history and stress, and how settling enough lets people act '
         'together.',
 'strat': 'Strategy for a future you cannot predict: rehearse several futures, map how things are changing, and keep '
          'options open.',
 'svc': 'Designing a service end to end: what people experience at each step and the behind-the-scenes work that '
        'makes it happen.',
 'sysdes': 'Design for whole systems and long time horizons: mapping big messes, imagining several futures, and '
           'finding where to intervene.',
 'teams': 'The team habits that let people raise bad news, learn fast, and organize around the flow of work instead '
          'of hierarchy.',
 'tgroup': 'Small unstructured groups where people learn about themselves and group dynamics by studying what '
           'happens between them in the moment.',
 'theoryu': "Otto Scharmer's Theory U: slow down, sense the whole situation with others, let go of old assumptions, "
            'then prototype what wants to emerge.',
 'trans': 'Design for long-term societal transitions toward sustainable futures, working across decades and many '
          'scales at once.',
 'transl': 'Learning that changes the frame, not only the content: often starting with a disorienting dilemma and '
           'leading to a new way of seeing.',
 'warm': "Nora Bateson's work on how living systems learn together across contexts, and Warm Data Labs: "
         'conversations that look at an issue through many parts of life at once.',
 'wtr': "Joanna Macy's group practice for facing ecological and social crisis: gratitude, honouring pain, seeing "
        'with new eyes, and going forth.'}

POL = {'adult': 'Leadership programmes that work with the hidden reasons reforms stall, without ranking staff by '
          'developmental stage.',
 'ai': 'Used in local government and public services for strength-based community planning and staff engagement.',
 'ar': 'Participatory research with residents to shape policy, and practitioner research inside public services.',
 'biosem': 'Conservation and land use that asks what a place means to the species living there, and design that '
           'works with animal signals such as light, sound and scent.',
 'bohm': 'Open conversations between agencies and communities, with no decision on the table, so hidden assumptions '
         'surface before they become policy.',
 'collab': 'Agencies working together in one place, with shared learning instead of shared targets, and residents '
           'with real seats at the table.',
 'conflict': 'Restorative approaches in courts, schools and housing, community mediation, and public meetings run so '
             'minority voices are heard.',
 'cop': 'Networks where practitioners from different agencies or cities learn from each other, and small groups of '
        'managers working through hard problems together.',
 'corp': 'Agencies, like companies, need protected space to try new services without starving the ones people rely '
         'on today.',
 'crisis': 'Emergency planning that works with volunteers, builds neighbourhood ties before disasters, and learns '
           'afterwards without blame.',
 'cx': 'Used to model epidemics, traffic, and markets, and to warn planners that a system can tip suddenly when it '
       'crosses a threshold.',
 'cxedu': 'Schools and training programmes that teach uncertainty, relationships and systems thinking alongside '
          'subject knowledge.',
 'cyb': "Designing services that can respond to the real variety of people's lives, instead of forcing everyone "
        'through one process.',
 'deval': 'Evaluating innovative programmes and policy experiments where outcomes are emergent and the model is '
          'still changing.',
 'dthink': "Used in government to understand residents' needs before designing, and to test ideas cheaply before "
           'committing money.',
 'econ': 'Doughnut-based city strategies, wellbeing budgets, and modelling that expects instability rather than '
         'equilibrium.',
 'exp': 'Learning as part of the job: reflective supervision, a review after each cycle of work, and training on '
        'real cases.',
 'fund': 'Multi-year flexible funding, portfolio budgets for missions, and grant terms that let providers change '
         'course when they learn something.',
 'grel': 'Used to train public leaders to work with authority and anxiety in large organizations, and to understand '
         'why reforms meet hidden resistance.',
 'host': "Participatory meetings, citizens' panels, and public sector staff trained to host conversations rather "
         'than present plans.',
 'improve': 'Quality improvement in public services, agile delivery, and adaptive management in development '
            'programmes.',
 'indig': 'Co-governance of land and water with Indigenous nations, free, prior and informed consent, and '
          'recognizing traditional knowledge as evidence on its own terms.',
 'labs': 'Teams inside government that test ideas with residents and change how money, rules and buying work, not '
         'just individual services.',
 'livsys': 'Regional planning around watersheds and bioregions, resilience planning for climate shocks, and circular '
           'economy strategies.',
 'meas': 'Swapping targets for learning reviews: report what changed and why, and judge services on the health of '
         'relationships, not activity counts.',
 'meta': 'Rarely a policy tool. It shows up as a frame for long-term risk, for questioning growth as the main goal, '
         'and for linking inner change to institutional change.',
 'moves': 'Supporting resident-led networks and mutual aid, and recognizing that policy change often follows shifts '
          'that movements make first.',
 'narr': 'Telling the story of a public problem so its real causes are visible, and giving staff and residents a '
         'shared story of why change is needed now.',
 'pd': 'Co-design with residents as decision-makers, not only informants, and design justice principles in public '
       'services.',
 'plumb': 'Contracts based on partnership instead of payment by results, policy written with the people who deliver '
          'it, and trust in frontline judgement.',
 'popedu': 'Community education that helps residents build their own view of an issue before they are consulted, so '
           'they shape policy as co-authors.',
 'posdev': 'Finding what already works for frontline staff and communities, and spreading it before bringing in '
           'outside solutions.',
 'power': 'Mapping who shapes a policy, which spaces are closed, invited or claimed, and where hidden norms keep '
          'people out.',
 'pubpol': 'The home field for government work. Read it with the money and accountability pathways, where budgets, '
           'contracts and targets decide what survives.',
 'reln': 'Shows up as a challenge rather than a tool: it asks policy to notice what its categories leave out and who '
         'is not in the room, including the land.',
 'ritual': 'Marking endings when programmes close or teams merge, and helping people through reorganizations instead '
           'of just redrawing the chart.',
 'selforg': 'Commons and co-operative governance of shared resources, participatory budgeting, and self-managing '
            'frontline teams in public services.',
 'semio': 'Public messaging, warning signs and symbols meant to last. The best-known case is marking nuclear waste '
          'sites so that people 10,000 years from now stay away.',
 'soma': 'Trauma-informed services and workplaces, support for staff in high-stress jobs, and public meetings where '
         'people feel settled enough to listen.',
 'strat': 'Scenario work before long-lived infrastructure or budget commitments, and Wardley maps before '
          'procurement.',
 'svc': 'Government digital services built around user needs, service standards, and blueprints that join the front '
        'line to the back office.',
 'sysdes': 'Futures and foresight units in government, systemic design labs, and Three Horizons conversations before '
           'long-term policy commitments.',
 'teams': 'Blameless reviews in public agencies, product teams that own a service end to end, and outcomes over '
          'outputs in digital delivery.',
 'tgroup': 'Mostly used to train public leaders and facilitators to notice group dynamics, rather than as a policy '
           'tool.',
 'theoryu': 'Co-sensing with residents and frontline staff before designing anything. u.lab is widely used by public '
            'teams. Social Presencing Theater is hosted as embodied sensing, not a way of gathering input.',
 'trans': 'Long-horizon planning for energy, food and mobility transitions, with many stakeholders and interventions '
          'at many scales.',
 'transl': 'Staff training that lets people rethink basic assumptions, not just learn new procedures, especially '
           'when a service is changing.',
 'warm': 'Warm Data Labs hosted with public staff and residents shift how people see an issue. Any policy follows '
         'from that changed ground in its own time, not from harvested findings.',
 'wtr': 'Rarely used directly in policy. It supports activists and staff facing burnout and grief, and work on '
        'climate anxiety.'}
