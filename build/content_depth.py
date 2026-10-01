"""Deeper article content for every pathway: plain explainer, how the tradition sees complexity, practice steps,
notes for other sectors, and key ideas with plain definitions.

Written 2026-10-01 from general knowledge of each field and the sources already linked on each pathway. All of it
is DRAFT: check it against sources before removing the Draft label in the app.

Keyed by short id (see content_atlas.SHORT). Fields:
  explainer  two plain paragraphs for "What it is" (skipped where content_atlas.EXPLAINERS already has one)
  lens       how this tradition sees complexity (skipped where content_atlas.PATH_LENS already has one)
  practice   3 to 5 first steps someone could actually take
  sectors    one line each for biz, ngo, health, edu, com (business, nonprofits, health, education, community groups)
  ideas      key ideas as (term, plain definition)
"""

D = {}

# ================================================================ Science and structure
D["cyb"] = dict(
    practice=["Draw one loop you are part of: what you do, what changes, how you find out, what you do next.",
              "Ask where the feedback is slow, missing, or filtered before it reaches the people who decide.",
              "Check requisite variety: list the situations you face, then the responses you have. Where the first list is longer, you will lose control.",
              "Name yourself as an observer. Write down what your position lets you see and what it hides."],
    sectors=dict(biz="Control systems, dashboards and management reporting are cybernetic, whether or not anyone calls them that.",
                 ngo="Programmes that hear from beneficiaries only once a year are steering with a very slow loop.",
                 health="Body regulation (temperature, blood sugar) was a founding example, and clinical audit is a feedback loop on care.",
                 edu="Gordon Pask's conversation theory treats teaching as two systems adjusting to each other.",
                 com="Neighbourhood groups steer well when people see the results of what they did quickly."),
    ideas=[("feedback", "When the result of an action loops back and shapes the next action."),
           ("requisite variety", "Ashby's law: to steer something, your responses need to be at least as varied as the situations you face."),
           ("second-order cybernetics", "Cybernetics that includes the observer: how you look is part of what you find."),
           ("viable system model", "Stafford Beer's model of the five functions any organization needs to survive and adapt."),
           ("homeostasis", "A system keeping something steady, like body temperature, by correcting drift.")])

D["cx"] = dict(
    explainer=["Complexity science studies systems made of many parts that interact, such as cells, ant colonies, cities and markets. "
               "The parts follow fairly simple local rules, yet together they produce patterns that none of them planned: traffic jams, "
               "epidemics, price bubbles, the shape of a flock.",
               "Researchers use computer models, network maps and mathematics to study how these patterns emerge and when they "
               "suddenly shift. The field's main lesson for practice is humility: you can often understand how a complex system "
               "behaves without being able to predict exactly what it will do next."],
    practice=["Pick a pattern you care about (waiting lists, rents, school choice) and ask which local rules people follow that add up to it.",
              "Sketch the network: who is connected to whom, and which few nodes hold many connections.",
              "Play with an agent-based model on Complexity Explorer or NetLogo before trusting a forecast.",
              "Look for tipping points: where would a small push cause a big shift?"],
    sectors=dict(biz="Supply chains and markets behave like networks; a failure at one hub spreads widely.",
                 ngo="Network maps show which partners hold a coalition together and where it would break.",
                 health="Epidemic models and hospital flow models come straight from this field.",
                 edu="Classrooms show emergence: the mood of a class is not any one pupil's doing.",
                 com="Local patterns like who shops where or who trusts whom are emergent and can shift quickly."),
    ideas=[("emergence", "When a whole shows patterns that none of its parts have on their own."),
           ("self-organization", "Order that arises from local interactions without anyone in charge."),
           ("agent-based model", "A computer simulation of many individual agents following rules, to see what patterns emerge."),
           ("network science", "The study of how things are connected and how connections shape what spreads."),
           ("tipping point", "A threshold where a small change flips a system into a different state.")])

D["sense"] = dict(
    practice=["Before deciding, sort the situation: is the answer known, knowable by experts, only visible in hindsight, or is it chaos?",
              "For complex issues, design three or four small, safe-to-fail probes instead of one big pilot.",
              "Agree in advance what you would amplify and what would make you stop each probe.",
              "Collect short stories from people affected and look for patterns across many of them, not one star example."],
    sectors=dict(biz="Used to separate operational problems with best practice from market shifts that need probing.",
                 ngo="Helps programmes stop reporting complex work as if it followed a logic model.",
                 health="Clinical protocols suit clear cases; patients with many conditions often sit in the complex domain.",
                 edu="School leaders use it to tell timetable problems apart from culture problems.",
                 com="Neighbourhood groups can run small experiments and keep what works."),
    ideas=[("cynefin", "A framework from Dave Snowden that sorts situations into clear, complicated, complex and chaotic. Each needs a different way of acting."),
           ("sensemaking", "Working out together what's going on in an unclear situation, before deciding what to do."),
           ("safe-to-fail", "A small experiment designed so that if it fails, the damage is small and you still learn."),
           ("probe-sense-respond", "In complex situations, act a little, see what happens, then adjust."),
           ("weak signals", "Early, faint signs of change that are easy to dismiss.")])

D["selforg"] = dict(
    explainer=["This pathway is about how groups can govern themselves without a single boss making every call. It gathers "
               "tested designs: sociocracy, where decisions are made by consent in linked circles; the Viable System Model, which "
               "shows the functions any organization needs; and Elinor Ostrom's principles for communities that manage shared "
               "resources like water or forests.",
               "Self-organizing does not mean structureless. These designs are often more explicit than a hierarchy about who "
               "decides what, how objections are heard, and how information travels. They spread authority to where the knowledge is."],
    lens="Complexity as distributed control: no single centre can know enough, so authority and feedback are designed to sit close to the work, linked so the whole can still adapt.",
    practice=["Map who actually decides what today, including the informal decisions.",
              "Try consent for one recurring decision: proceed unless someone has a reasoned objection that it would cause harm.",
              "Write down the domain of one team: what it can decide without asking.",
              "If you share a resource, check it against Ostrom's eight principles, such as clear boundaries and local monitoring."],
    sectors=dict(biz="Buurtzorg and Haier show self-managing teams at scale; many firms use consent in leadership teams.",
                 ngo="Small charities and co-ops use sociocracy to share decisions with staff and members.",
                 health="Self-managing nurse teams in home care are the best-known example.",
                 edu="Student councils and staff circles can run on consent rather than majority vote.",
                 com="Community land trusts, housing co-ops and allotments are classic commons."),
    ideas=[("sociocracy", "A way of governing with consent decisions in linked circles, so every voice has a route."),
           ("consent", "A decision passes unless someone has a reasoned objection that it would cause harm, not when everyone agrees."),
           ("commons", "A shared resource managed by the community that uses it."),
           ("polycentric governance", "Many centres of decision at different scales, overlapping and checking each other."),
           ("viable system model", "Stafford Beer's model of the five functions any organization needs to survive and adapt.")])

D["pubpol"] = dict(
    explainer=["This pathway asks how government can work when the problems it faces are tangled and changing. Instead of "
               "setting targets and rolling out a fixed plan, it treats public services as systems that need to learn: trying "
               "things, listening to people, building relationships and adjusting.",
               "It brings together ideas like wicked problems, leverage points and mission-oriented policy, and practical "
               "movements like Human Learning Systems and the relational state. The common thread is that outcomes come from "
               "many actors working together, so the state's job is often to steward the system rather than control it."],
    lens="Complexity as wicked problems: issues with no final definition, no single owner, and no solution that stays solved, so policy has to keep learning.",
    practice=["Pick one service and ask who else shapes the outcome it is measured on.",
              "Replace one target with a learning question that staff and residents review together every few months.",
              "Spend a day with frontline staff before writing the next policy paper.",
              "Fund a small portfolio of approaches rather than one pilot, and agree how you will learn across them."],
    sectors=dict(biz="Firms that deliver public contracts feel this most: payment by results versus alliance contracts.",
                 ngo="Charities are often the frontline of public services and can push for learning-based commissioning.",
                 health="Integrated care systems are attempts to run health and care as one learning system.",
                 edu="Education policy that sets curriculum but trusts schools to adapt sits in this space.",
                 com="Community groups are partners, not just consultees, in the relational state."),
    ideas=[("wicked problem", "A problem with no clear definition, no right answer, and no point where it is solved for good."),
           ("leverage point", "A place in a system where a small shift produces big change, from Donella Meadows."),
           ("human learning systems", "An approach to public management built on learning, relationships and system stewardship instead of targets."),
           ("mission-oriented policy", "Policy organized around a bold, concrete goal that many sectors work toward."),
           ("stewardship", "Looking after the health of a whole system rather than controlling its parts.")])

D["sysdes"] = dict(
    explainer=["Systemic design takes the tools of design, like drawing, prototyping and working with users, and applies them "
               "to whole systems such as food, mobility or care. Designers make big visual maps, sometimes called gigamaps, so "
               "a group can see a whole system at once and find where to act.",
               "Futures work is its companion. Methods like Three Horizons, scenarios and futures literacy help people imagine "
               "several possible futures and use them to make better choices today, instead of betting on one forecast."],
    lens="Complexity as a mess to be seen whole: map the system richly enough that people can find leverage, and use several futures to loosen today's assumptions.",
    practice=["Make a big shared map of a system with the people in it, on one wall, before choosing an intervention.",
              "Run a Three Horizons conversation: what is fading, what is emerging, what is the bridge between them?",
              "Write two or three short scenarios and test your plan against each.",
              "Look for the pockets of the future already present today."],
    sectors=dict(biz="Strategy teams use scenarios and horizon scanning to stress-test plans.",
                 ngo="System maps help coalitions agree where each organization fits.",
                 health="Gigamaps of patient pathways show where handoffs fail.",
                 edu="Futures literacy is taught in schools and universities through UNESCO labs.",
                 com="Community futures workshops let residents imagine their place in 30 years."),
    ideas=[("gigamapping", "Making very large, detailed visual maps of a system so a group can see it whole."),
           ("three horizons", "A framework that looks at the fading present, the emerging future, and the transition between them."),
           ("futures literacy", "The skill of using imagined futures to understand and act in the present."),
           ("scenario", "A coherent story of a possible future, used to test plans, not to predict."),
           ("foresight", "Systematic thinking about possible futures to inform decisions now.")])

D["econ"] = dict(
    explainer=["Mainstream economics often pictures the economy as a machine that settles into balance. Complexity economics "
               "sees it instead as an ecosystem that never stops changing: people and firms learn, copy each other and invent, "
               "so the economy keeps creating new patterns, booms and crashes.",
               "New economic models build on this. Kate Raworth's Doughnut asks how to meet everyone's needs without overshooting "
               "the planet's limits. Others look at wellbeing economies and post-growth. Together they argue that the goal of an "
               "economy is a choice, and that it should be set openly."],
    practice=["Draw your city or organization's Doughnut: which social needs fall short, which planetary limits are overshot?",
              "Ask where increasing returns lock in a winner, and whether that is healthy.",
              "Swap one growth metric for a wellbeing indicator and see what changes in the conversation.",
              "Look at who benefits from a policy over time, not only at launch."],
    sectors=dict(biz="Platform markets show increasing returns: the leader gets stronger simply by being ahead.",
                 ngo="Wellbeing economy alliances bring charities into economic policy.",
                 health="Health is a big part of any wellbeing economy and of the social foundation in the Doughnut.",
                 edu="Rethinking Economics and CORE teach economics with these ideas built in.",
                 com="Local Doughnut groups and community wealth building apply it at neighbourhood scale."),
    ideas=[("increasing returns", "When being ahead makes it easier to get further ahead, so small early leads lock in."),
           ("doughnut economics", "Kate Raworth's model: meet everyone's needs without overshooting the planet's limits."),
           ("bounded rationality", "Herbert Simon's idea that people decide with limited time, information and attention."),
           ("equilibrium", "A state of balance. Complexity economics argues real economies rarely settle into one."),
           ("wellbeing economy", "An economy designed to deliver human and ecological wellbeing rather than growth for its own sake.")])

D["strat"] = dict(
    explainer=["Strategy under uncertainty starts from an honest admission: nobody can predict the future well enough to plan "
               "around a single forecast. Instead, it uses tools that prepare an organization for several futures at once.",
               "Scenarios rehearse plausible futures so leaders notice early signs. Wardley Maps show how the parts of a "
               "business or service evolve from new to commodity, so you know what to build and what to buy. Antifragility asks "
               "how to design things that gain from shocks rather than break."],
    lens="Complexity as an open future: plans must hold up across several possible worlds, and strategy is a way of noticing and responding, not a fixed route.",
    practice=["Write two to four scenarios with people who disagree, then ask what you would do in each.",
              "Draw a Wardley Map of one service: what users need, and how evolved each component is.",
              "List decisions that are hard to reverse and slow them down; speed up the easy-to-reverse ones.",
              "Name the early signs that would tell you which scenario is unfolding, and watch for them."],
    sectors=dict(biz="Shell's scenarios are the classic case; Wardley Mapping is widely used in tech strategy.",
                 ngo="Scenarios help charities plan when funding and policy may shift sharply.",
                 health="Pandemic preparedness is scenario work; the plans that held up were the flexible ones.",
                 edu="Universities use scenarios to think about demographics and technology.",
                 com="Transformative scenario planning brought opposing groups together in South Africa."),
    ideas=[("scenario planning", "Rehearsing several plausible futures to make better decisions now."),
           ("wardley mapping", "A map of a value chain showing how each component evolves from novel to commodity."),
           ("antifragility", "Nassim Taleb's word for things that get stronger from shocks and stress."),
           ("optionality", "Keeping choices open so you can act when the future becomes clearer."),
           ("transformative scenario planning", "Adam Kahane's method where opponents build scenarios together to change the situation, not just adapt to it.")])

D["fund"] = dict(
    explainer=["Most money in organizations and government is tied to fixed annual budgets and detailed plans. That makes it "
               "hard to change course when you learn something. This pathway collects ways to let money follow learning instead.",
               "Beyond Budgeting replaces the annual budget with rolling forecasts and decisions made closer to the work. Portfolio "
               "approaches fund several experiments at once and move money toward what works. Trust-based philanthropy gives "
               "grantees flexible, multi-year money and lighter reporting."],
    lens="Complexity as money that has to adapt: when outcomes are uncertain, funding works best in portfolios and rolling cycles that can follow what is learned.",
    practice=["Find one budget line that could move from annual to rolling review.",
              "Fund three small, different approaches to one problem instead of one big bet.",
              "Ask a grantee what reporting they would drop if they could, and drop it.",
              "Agree up front how money will move when you learn something, so changing course is not a failure."],
    sectors=dict(biz="Handelsbanken and Equinor run without traditional annual budgets.",
                 ngo="Unrestricted, multi-year grants let charities adapt; trust-based funders lead this.",
                 health="Pooled budgets across health and care follow patients instead of departments.",
                 edu="Schools with flexible budgets can respond to what pupils need mid-year.",
                 com="Participatory grant-making lets residents decide where community money goes."),
    ideas=[("beyond budgeting", "Running an organization without fixed annual budgets, using rolling forecasts and devolved decisions."),
           ("portfolio approach", "Funding several linked experiments together and managing them as a whole."),
           ("trust-based philanthropy", "Grant-making built on flexible money, light reporting and shared power with grantees."),
           ("rolling forecast", "A forecast updated regularly instead of fixed once a year."),
           ("unrestricted funding", "Money a grantee can spend on whatever the work needs.")])

D["meas"] = dict(
    explainer=["When a number becomes a target, people start working to the number instead of the purpose behind it. This "
               "pathway explains why that happens and what to do instead. Campbell's and Goodhart's laws describe the distortion; "
               "Jerry Muller's The Tyranny of Metrics collects the evidence.",
               "The alternative is not to stop measuring but to measure for learning. Public value thinking asks what a service "
               "is for and who it answers to. Accountability for learning holds people to account for reflecting honestly and "
               "improving, not for hitting numbers they do not control."],
    lens="Complexity as outcomes nobody controls alone: numbers can inform learning, but used as targets in a complex system they distort the work they are meant to measure.",
    practice=["List your targets and ask, for each one, how someone could hit it while making things worse.",
              "Turn one target into a question you review together: what did we learn, and what will we try next?",
              "Collect a few stories alongside the numbers so you can see what the numbers miss.",
              "Ask who the measures are for: the people served, the staff, or the funder."],
    sectors=dict(biz="Sales targets that encourage mis-selling are a classic case of Goodhart's law.",
                 ngo="Funders and charities can agree learning questions instead of output counts.",
                 health="Waiting-time targets have led to gaming, such as patients held in ambulances.",
                 edu="Test-score targets narrow teaching to the test.",
                 com="Community groups can track what matters to members, not just attendance."),
    ideas=[("goodhart's law", "When a measure becomes a target, it stops being a good measure."),
           ("campbell's law", "The more a number is used for decisions, the more it gets corrupted and corrupts the work."),
           ("public value", "Mark Moore's idea that public managers should create value the public cares about, with legitimacy and capacity to deliver it."),
           ("accountability for learning", "Holding people to account for learning and improving, not for numbers they do not control."),
           ("gaming", "Hitting a target in ways that defeat its purpose.")])

D["plumb"] = dict(
    explainer=["New ideas about complexity often die in the ordinary machinery of government: procurement rules, contracts, "
               "budgets, audits, and job descriptions. This pathway is about that machinery, which some people call the plumbing.",
               "Michael Lipsky showed that frontline workers make policy every day through the choices they make. Experimentalist "
               "governance sets broad goals and lets local units find their way, reviewing together. Jennifer Pahlka's Recoding "
               "America shows how layers of rules make simple services fail. The lesson: if you want change to last, change the plumbing."],
    lens="Complexity in the machinery: rules, contracts and routines interact in ways no one designed, and they quietly decide which new ideas survive.",
    practice=["Trace one simple request through every rule and form it touches, and count the steps.",
              "Ask procurement to sit in on the design of a service, not just the tender.",
              "Try an alliance contract where providers share one outcome instead of competing.",
              "Ask frontline staff which rule they work around most, and why."],
    sectors=dict(biz="Suppliers to government live with this plumbing and can help redesign contracts.",
                 ngo="Charities feel the effects of short contracts and payment by results.",
                 health="Commissioning rules decide whether health and care can work as one.",
                 edu="Funding formulas and inspection regimes shape what schools can try.",
                 com="Grant rules and licensing decide whether community groups can act quickly."),
    ideas=[("street-level bureaucracy", "Michael Lipsky's insight that frontline workers effectively make policy through daily choices."),
           ("experimentalist governance", "Set broad goals centrally, let local units try ways to meet them, and review together."),
           ("relational commissioning", "Buying services through ongoing relationships and shared goals rather than fixed specifications."),
           ("alliance contract", "One contract where several providers share responsibility for an outcome."),
           ("regulatory sandbox", "A safe space where new approaches can be tested under relaxed rules with close watching.")])

D["teams"] = dict(
    explainer=["Most complex work happens in teams. This pathway is about the conditions that let a team learn: people feel "
               "safe to raise problems and admit mistakes, the team is organized around the flow of work, and it measures "
               "success by outcomes for users rather than tasks finished.",
               "Amy Edmondson's research on psychological safety showed that the best hospital teams reported more errors, "
               "because they talked about them. Team Topologies offers a few simple team types and ways they interact. Sense "
               "and Respond applies these ideas to whole organizations."],
    lens="Complexity in the team: learning depends on people speaking up and on how teams connect, so the structure of conversations matters as much as the structure of tasks.",
    practice=["Start a meeting by inviting the problem nobody has raised yet, and thank whoever raises it.",
              "Run a blameless review of something that went wrong: what happened, what made sense at the time, what will change.",
              "Ask the team what outcome for users it is trying to change this quarter.",
              "Map how your team depends on others and cut one handoff."],
    sectors=dict(biz="Common in tech and product teams; Google's Project Aristotle highlighted psychological safety.",
                 ngo="Small teams under pressure benefit from blameless reviews and clear outcomes.",
                 health="Edmondson's research began in hospital teams; speaking up saves lives.",
                 edu="Teaching teams that share failures openly improve faster.",
                 com="Volunteer groups need the same safety to raise problems early."),
    ideas=[("psychological safety", "A shared belief that the team is safe for speaking up, asking questions and admitting mistakes."),
           ("blameless review", "Looking at what went wrong to learn, without seeking someone to punish."),
           ("team topologies", "A small set of team types and ways of interacting, to organize around the flow of work."),
           ("outcomes over outputs", "Judging work by the change it makes for people, not by how much was produced."),
           ("teaming", "Edmondson's word for forming and working in teams on the fly.")])

D["corp"] = dict(
    explainer=["Established organizations are good at running what they already do and bad at inventing what comes next. "
               "This pathway collects research on why, and on how some have managed both.",
               "Disruptive innovation explains how newcomers win by starting where incumbents are not looking. Ambidextrous "
               "organizations protect new units from the old ones while sharing what helps. Open innovation looks outside for "
               "ideas. Haier's microenterprises go furthest, breaking a giant firm into thousands of small self-managing businesses."],
    lens="Complexity as constant renewal: an organization is a living system that must keep exploring while exploiting what works, or its environment will move on without it.",
    practice=["Split your work into run and explore, and protect a small budget for exploring.",
              "Ask where a cheaper, simpler competitor could start today, and talk to those customers.",
              "Invite one outside partner to solve a problem you have kept internal.",
              "Try a small unit with its own customers and its own profit and loss."],
    sectors=dict(biz="This is home ground: Christensen, O'Reilly and Tushman, Chesbrough and Haier.",
                 ngo="Large charities face the same tension between their core programmes and new approaches.",
                 health="Health systems need protected space for new models of care alongside the old.",
                 edu="Universities set up separate units for online learning to avoid being smothered.",
                 com="Community groups can spin off new projects without risking the core."),
    ideas=[("disruptive innovation", "When a simpler, cheaper offer starts at the bottom of a market and moves up until it displaces leaders."),
           ("ambidexterity", "Running the current business well while exploring new ones."),
           ("open innovation", "Using ideas and partners from outside the organization."),
           ("rendanheyi", "Haier's model of thousands of small, self-managing units close to customers."),
           ("exploit and explore", "The tension between using what works and searching for what might work.")])

D["collab"] = dict(
    explainer=["Big social problems are not owned by any one organization. This pathway is about how many organizations, "
               "public, private and community, can work on one shared problem together.",
               "Collective impact (2011) set out five conditions, including a common agenda and a backbone organization. Practice "
               "since then has moved on: Collective Impact 3.0 shifts from management to movement building, and the field now "
               "puts equity and community power at the centre."],
    lens="Complexity as shared problems: no single actor can solve them, so progress comes from aligning many actors around learning, with the most affected people holding real power.",
    practice=["Map who already works on the problem and invite the people most affected into the first meeting.",
              "Agree a few shared learning questions before agreeing shared indicators.",
              "Fund a small backbone team whose job is to connect, not to control.",
              "Check who holds decision power in the partnership and whether residents have real seats."],
    sectors=dict(biz="Firms join place-based partnerships as employers, funders and suppliers.",
                 ngo="Charities often host the backbone function.",
                 health="Health partnerships with councils and charities tackle causes of ill health.",
                 edu="Strive in Cincinnati linked schools, colleges and services around children's progress.",
                 com="Community organizations bring legitimacy and knowledge the institutions lack."),
    ideas=[("collective impact", "Many organizations working on one problem with a common agenda and a backbone team."),
           ("backbone organization", "A small team that supports a partnership by connecting, convening and keeping data."),
           ("common agenda", "A shared understanding of the problem and the change being sought."),
           ("network weaving", "Deliberately building connections between people so a network can act."),
           ("community power", "Residents holding real decision-making power, not only a voice.")])

# ================================================================ Relational and living
D["reln"] = dict(
    explainer=["This pathway gathers thinkers who say we understand the world best through relationships, not by breaking "
               "it into separate parts. Gregory Bateson traced how mind is spread across organism and environment. Others "
               "question the idea that humans stand apart from the rest of life.",
               "It also asks hard questions about modern ways of knowing. Bayo Akomolafe and Vanessa Machado de Oliveira ask how "
               "even our efforts to fix things can repeat the patterns that caused harm, and invite slowing down and staying "
               "with difficulty rather than rushing to solutions."],
    lens="Complexity as relationship: nothing exists on its own, and what something is depends on its connections, including its connection to whoever is looking.",
    practice=["Take one problem and describe it from five contexts: family, work, health, money, place.",
              "Notice when you reach for a quick solution, and stay one more conversation with the question.",
              "Ask what the situation looks like from beings or places with no voice in the room.",
              "Read one text slowly with others, and talk about what it did to you, not just what it said."],
    sectors=dict(biz="Shows up in regenerative business and in questioning growth as a default.",
                 ngo="Invites charities to examine how help can repeat the harms it set out to fix.",
                 health="Relational care sees illness through a person's whole web of relationships.",
                 edu="Relational pedagogy treats learning as something that happens between people.",
                 com="Community work that starts from relationships rather than needs assessments."),
    ideas=[("ecology of mind", "Bateson's idea that mind is a pattern across organism and environment, not something inside a head."),
           ("transcontextual", "A problem lives in many contexts at once, and each shapes the others."),
           ("hospicing modernity", "Caring for a dying way of life well, so something new can emerge, rather than propping it up."),
           ("post-humanism", "Questioning the idea that humans stand apart from and above the rest of life."),
           ("agential realism", "Karen Barad's view that things come into being through their relationships.")])

D["warm"] = dict(
    explainer=["Nora Bateson, daughter of Gregory Bateson, carries his ecology of mind into practice. Her central idea is "
               "Warm Data: information about how the parts of a system relate, which you can only find by looking across many "
               "contexts at once, such as family, economy, health and culture.",
               "Warm Data Labs are gatherings where people move between small conversations, each framed by a different context, "
               "and talk about an issue from their own lives. There is no goal and no output. The aim is that people start to "
               "perceive the issue differently, and change follows from that."],
    lens="Complexity as interdependence across contexts: a problem lives in many contexts at once, and learning happens between them, in what Bateson calls symmathesy.",
    practice=["Pick an issue and talk about it with a friend through three contexts in turn: family, money, health.",
              "Notice when you want a takeaway, and let the conversation stay open instead.",
              "Attend a Warm Data Lab before trying to host one; host training is offered by the Bateson Institute.",
              "Keep a note of patterns that show up across contexts, not inside one."],
    sectors=dict(biz="Used in leadership retreats to loosen fixed views of a problem.",
                 ngo="Helps community programmes see how one issue tangles with others.",
                 health="Shows how illness is bound up with work, family and place.",
                 edu="Bateson writes on education for a confusing future; labs are run with teachers and students.",
                 com="Labs are often hosted locally, open to anyone in a neighbourhood."),
    ideas=[("warm data", "Information about how parts of a system relate, gathered across many contexts at once."),
           ("symmathesy", "Living things learn and change together, in context. No part learns alone."),
           ("transcontextual", "A problem lives in many contexts at once: family, economy, health, culture."),
           ("aphanipoiesis", "Bateson's word for the unseen ways things come together toward vitality."),
           ("warm data lab", "A gathering where people talk about an issue through many contexts in turn, with no set outcome.")])

D["indig"] = dict(
    explainer=["Indigenous and land-based knowledge is knowledge held by peoples in long relationship with particular lands, "
               "waters and kin. It is carried in story, ceremony, language, practice and law, and it treats reciprocity and "
               "responsibility as part of knowing.",
               "This pathway points to Indigenous authors who write for wider audiences, like Robin Wall Kimmerer and Tyson "
               "Yunkaporta. It is not a set of techniques to borrow. Engaging well means relationship, consent, credit and "
               "shared power, guided by the communities whose knowledge it is."],
    lens="Complexity as kinship and pattern: knowledge lives in relationship with land and community over generations, and right relationship is part of what makes it true.",
    practice=["Learn whose land you are on, and what the nations there ask of visitors and neighbours.",
              "Read Indigenous authors in their own words before reading about them.",
              "When a project draws on Indigenous knowledge, ask who was consulted, who consented, and who benefits.",
              "Support Indigenous-led organizations with money and decision power, not only invitations."],
    sectors=dict(biz="Free, prior and informed consent is a standard for projects on Indigenous land.",
                 ngo="Conservation groups are shifting toward Indigenous-led stewardship.",
                 health="Culturally grounded care, led by Indigenous health services, improves outcomes.",
                 edu="Land-based education and Indigenous science sit alongside Western science in some curricula.",
                 com="Co-management of land and water shares authority between nations and governments."),
    ideas=[("reciprocity", "Taking only what is given, and giving back in return, as a principle of relationship."),
           ("honorable harvest", "Kimmerer's guidelines for taking from the land with respect, so it can keep giving."),
           ("two-eyed seeing", "Seeing with the strengths of Indigenous and Western knowledge together, from Mi'kmaw Elder Albert Marshall."),
           ("free, prior and informed consent", "The right of Indigenous peoples to agree or refuse before projects affect their lands."),
           ("land-based knowledge", "Knowledge that comes from long relationship with a particular place.")])

D["theoryu"] = dict(
    explainer=["Theory U describes a journey for groups facing change. Instead of jumping from a problem to a solution, a "
               "group goes down the U: suspending habitual judgements, sensing the whole system, and connecting at the bottom "
               "with what wants to emerge. Then it comes up the other side by prototyping and building.",
               "Otto Scharmer and the Presencing Institute developed it from interviews with many leaders and thinkers. Social "
               "Presencing Theater, created by Arawana Hayashi, uses simple movement so groups can sense a system with their "
               "bodies. The free u.lab course has reached many public-sector teams."],
    lens="Complexity as the future emerging: the quality of attention in a group shapes what it can bring into being, so change begins with how people see.",
    practice=["Before your next project, go on a learning journey to see the system from the other side.",
              "Practise listening at four levels: downloading, factual, empathic and generative.",
              "Try a short stuckness-to-movement exercise from Social Presencing Theater.",
              "Prototype quickly once an idea crystallizes, and learn from real use."],
    sectors=dict(biz="Used in leadership programmes and organizational change.",
                 ngo="Coalitions use u.lab hubs to build shared awareness.",
                 health="Health systems have run Theory U journeys with patients and staff.",
                 edu="u.school applies it to education transformation.",
                 com="Community hubs run u.lab locally."),
    ideas=[("presencing", "Sensing and acting from the highest future possibility, from presence plus sensing."),
           ("theory u", "A change process that moves through seeing, sensing and presencing before prototyping."),
           ("downloading", "Listening that only confirms what you already think."),
           ("learning journey", "Visiting places and people in a system to see it freshly."),
           ("social presencing theater", "Arawana Hayashi's movement practice for sensing a system with the body.")])

D["meta"] = dict(
    explainer=["The metacrisis is the idea that climate breakdown, inequality, polarization and other crises are not separate "
               "problems but symptoms of a deeper pattern in how modern culture perceives, values and makes sense of the world.",
               "Thinkers here, including Iain McGilchrist, Jonathan Rowson and Zak Stein, look at attention, meaning, education "
               "and the health of public sensemaking. Their claim is that technical fixes alone will not be enough without "
               "changes in how people see, and that this inner work is also public work."],
    lens="Complexity as one pattern beneath many crises: the way a culture attends to the world shapes the problems it produces and the solutions it can see.",
    practice=["Pick two crises you care about and ask what they have in common at the level of values and attention.",
              "Notice where your own attention goes in a day, and what that trains you to see.",
              "Join or host a small reading circle on Perspectiva or McGilchrist and discuss what it changes in your work.",
              "Ask what an institution would need to sense the long term, not just the next cycle."],
    sectors=dict(biz="Raises questions about attention-harvesting business models.",
                 ngo="Asks charities whether single-issue campaigns can address shared roots.",
                 health="Links mental health to meaning and the wider culture.",
                 edu="Education for the metacrisis focuses on wisdom and sensemaking, not only skills.",
                 com="Local groups explore meaning and practice together in study circles."),
    ideas=[("metacrisis", "The idea that many crises share one root in how modern culture sees and makes meaning."),
           ("polycrisis", "Several crises interacting so the whole is worse than the sum."),
           ("meaning crisis", "John Vervaeke's term for the loss of shared ways to make sense of life."),
           ("hemisphere hypothesis", "McGilchrist's argument that culture has come to favour a narrow, grasping kind of attention."),
           ("sensemaking", "Working out together what's going on in an unclear situation, before deciding what to do.")])

D["livsys"] = dict(
    explainer=["Living systems thinking starts from what life does: living things make and remake themselves, depend on each "
               "other, and adapt to change. Maturana and Varela called this self-making autopoiesis. Fritjof Capra and others "
               "showed how the same principles apply to ecosystems and human communities.",
               "Two practical strands grew from it. Resilience thinking studies how social-ecological systems absorb shocks and "
               "reorganize. Regenerative design asks how human activity can leave places healthier than before, not just do "
               "less harm."],
    lens="Complexity as life itself: self-making networks that keep renewing themselves and their surroundings.",
    practice=["Treat your place as a living system: map flows of water, food, energy and people.",
              "Ask of any project whether it leaves the place more or less able to renew itself.",
              "Look for slow variables, like soil health or trust, that shape what is possible later.",
              "Design for diversity and redundancy, not just efficiency."],
    sectors=dict(biz="Regenerative business and circular economy apply these ideas.",
                 ngo="Conservation and land groups use resilience thinking.",
                 health="One Health links human, animal and environmental health.",
                 edu="Ecoliteracy brings living-systems thinking into schools.",
                 com="Bioregional and transition groups organize around their watershed or region."),
    ideas=[("autopoiesis", "Self-making: living systems produce and maintain themselves."),
           ("resilience", "A system's capacity to absorb shocks and reorganize while keeping its core functions."),
           ("regenerative design", "Design that leaves places and communities healthier than before."),
           ("bioregion", "A region defined by natural features like a watershed, rather than by political lines."),
           ("adaptive cycle", "C.S. Holling's model of growth, conservation, release and reorganization in living systems.")])

D["biosem"] = dict(
    explainer=["Biosemiotics studies life as a world of signs. A bacterium swims toward sugar because it reads a chemical "
               "gradient as a sign of food. A bird hears an alarm call and flees. A cell responds to a hormone. In each case "
               "something stands for something else to a living being, and the being acts on it.",
               "The idea goes back to Jakob von Uexküll, who said every animal lives in its own Umwelt: the slice of the world "
               "its senses and needs make meaningful. A tick's world has only a few signs in it. Biosemiotics, developed in "
               "Copenhagen and Tartu, argues that meaning is part of nature, not something only human minds add."],
    lens="Complexity as interpretation: living systems are webs of beings reading signs from each other and their surroundings, so to understand a living system you ask what things mean to whom.",
    practice=["Pick an animal near you and list what its world is made of: what it notices, what it ignores, what signals danger or food.",
              "When planning a green space, ask what the place means to the species that use it, not only how many there are.",
              "Read Uexküll's short Foray into the Worlds of Animals and Humans with a group and walk a place through different Umwelten.",
              "In a reintroduction or conservation project, map what the species means to local people as well as what it needs."],
    sectors=dict(biz="Sensory design and animal welfare draw on how other species perceive.",
                 ngo="Conservation groups use Umwelt thinking to reduce human-wildlife conflict.",
                 health="Cell signalling and the immune system are prime examples of biological sign processes.",
                 edu="A strong bridge between biology, philosophy and the humanities.",
                 com="Umwelt-based walks help residents see their neighbourhood through other species."),
    ideas=[("umwelt", "The world as a particular animal experiences it: only what its senses and needs make meaningful."),
           ("biosemiotics", "The study of signs and meaning in living systems, from cells to ecosystems."),
           ("semiotic freedom", "How many ways a living thing can respond to the same sign; it tends to grow through evolution."),
           ("ecosemiotics", "The study of how signs connect cultures and ecosystems, developed in Tartu."),
           ("semiosis", "The process by which something comes to stand for something else to someone.")])

D["semio"] = dict(
    explainer=["Semiotics is the study of signs: anything that stands for something else to someone. Words, pictures, traffic "
               "lights, smoke meaning fire, a uniform meaning authority. Charles Sanders Peirce described three kinds: icons, which "
               "resemble what they stand for; indexes, which are connected to it, like a footprint; and symbols, which work by "
               "convention, like most words.",
               "From there semiotics looks at how whole cultures run on sign systems. Saussure showed that meaning comes from "
               "differences within a system. Yuri Lotman described the semiosphere, the shared space of meaning a culture lives "
               "in. Eduardo Kohn extends the question beyond humans: in How Forests Think, he shows how the Amazonian forest is "
               "full of other beings interpreting signs."],
    lens="Complexity as meaning-making: what a sign means depends on a three-way relation between the sign, what it points to and whoever reads it, so meaning is always in motion and different for different readers.",
    practice=["Take one public form or sign and ask three different people what it tells them; compare.",
              "Sort the signs in a service into icons, indexes and symbols, and check which depend on knowledge some users lack.",
              "When a message must last, use several kinds of sign together and repeat it in more than one channel.",
              "Ask what an official category (like 'household' or 'disability') makes visible and what it hides."],
    sectors=dict(biz="Branding and user interface design are applied semiotics.",
                 ngo="Campaigns test how symbols land with different audiences.",
                 health="Warning labels and patient information depend on signs being read as intended.",
                 edu="Media literacy teaches students to read images and texts as sign systems.",
                 com="Public art and place names carry meanings that differ between communities."),
    ideas=[("semiotics", "The study of signs: anything that stands for something else to someone."),
           ("icon, index, symbol", "Peirce's three kinds of sign: by resemblance, by connection, and by convention."),
           ("signifier and signified", "Saussure's split between the form of a sign and the concept it carries."),
           ("semiosphere", "Lotman's term for the shared space of signs a culture lives in."),
           ("semiosis", "The process by which something comes to stand for something else to someone.")])

D["bohm"] = dict(
    explainer=["Bohm Dialogue is a way for a group to think together. People sit in a circle, often for a long time, with no "
               "agenda and no decision to make. The aim is to notice how thought moves in the group, and to suspend your "
               "assumptions: hold them up to look at, rather than defend them or drop them.",
               "The physicist David Bohm developed it late in life because he saw that collective thought is full of hidden "
               "assumptions that cause conflict. William Isaacs and the MIT Dialogue Project brought it into organizations, and "
               "Peter Senge made it part of the learning organization."],
    lens="Complexity as collective thought: meaning flows through a group and shapes what it can see, so change begins by attending to how the group thinks.",
    practice=["Gather 10 to 30 people for at least an hour with no agenda except to talk and listen.",
              "When you feel a strong reaction, say what it is rather than arguing from it.",
              "Practise suspension: notice an assumption, say it aloud, and look at it together.",
              "Meet regularly; the practice deepens over several sessions."],
    sectors=dict(biz="Used to rebuild trust between union and management and in leadership teams.",
                 ngo="Coalitions use it before strategy decisions to surface hidden assumptions.",
                 health="Dialogue groups help clinicians and managers hear each other.",
                 edu="Dialogue circles in schools and universities practise listening.",
                 com="Community dialogues across divides, with no decision on the table."),
    ideas=[("dialogue", "A shared inquiry where meaning flows through a group, from the Greek for 'through the word'."),
           ("suspension", "Holding an assumption up to look at, without defending it or dropping it."),
           ("proprioception of thought", "Bohm's idea of noticing your own thinking as it happens, the way you sense your body."),
           ("thinking together", "Isaacs' phrase for groups that think as a whole rather than trade fixed positions."),
           ("container", "The shared space of trust that lets a group hold difficult conversation.")])

D["tgroup"] = dict(
    explainer=["A T-group (training group) is a small group that meets with no agenda except to learn from what happens "
               "between its members, here and now. People give and receive feedback on how they come across and notice how "
               "the group forms, struggles and works.",
               "It began in 1946 when Kurt Lewin's team found that participants learned most when they joined staff discussions "
               "of their own behaviour. The National Training Laboratories followed in 1947. T-groups shaped organization "
               "development and live on in courses like Stanford's Interpersonal Dynamics, known as Touchy Feely."],
    lens="Complexity in the here and now: a group's behaviour emerges from its members' interactions, and you learn it best by studying it as it happens.",
    practice=["Join a structured T-group lab with trained facilitators; do not improvise one on colleagues.",
              "Practise giving feedback about specific behaviour and its effect on you, not about character.",
              "In meetings, notice who speaks, who is interrupted and what is avoided.",
              "Ask for feedback on one habit and try a small change."],
    sectors=dict(biz="The root of much management and leadership training.",
                 ngo="Builds the self-awareness facilitators need.",
                 health="Group-based learning for clinicians handling difficult relationships.",
                 edu="Interpersonal Dynamics at Stanford and similar courses.",
                 com="Helps organizers notice group dynamics and power."),
    ideas=[("here and now", "Paying attention to what is happening in the group right now, not to outside topics."),
           ("feedback", "Telling someone the effect their behaviour had on you, specifically and kindly."),
           ("group dynamics", "Kurt Lewin's term for the forces that shape how groups behave."),
           ("t-group", "A small training group that learns from its own interaction."),
           ("laboratory method", "Learning by experimenting with behaviour in a safe, temporary setting.")])

D["grel"] = dict(
    explainer=["Group Relations studies how groups and organizations behave below the surface: the anxieties, fantasies and "
               "unspoken assumptions that shape how people take up authority and roles. It grew from Wilfred Bion's work with "
               "groups and the Tavistock Institute.",
               "Its main method is the conference, a temporary organization where members study authority and leadership as "
               "they happen. The Leicester Conference has run since 1957. The insight for practice: organizations often "
               "resist the very change they commission, for reasons nobody says out loud."],
    lens="Complexity below the surface: groups carry unconscious patterns of anxiety and defence that shape what an organization can do.",
    practice=["Attend a Group Relations conference before applying the ideas to others.",
              "Ask what anxiety a structure or procedure might be protecting people from.",
              "Notice when a group seems to be acting on an unspoken assumption, such as waiting for a leader to save it.",
              "Separate the person from the role: what is being asked of the role?"],
    sectors=dict(biz="Executive education and consulting draw on systems psychodynamics.",
                 ngo="Helps leaders understand projections from staff and funders.",
                 health="Isabel Menzies Lyth's study of nurses showed how hospital routines defended against anxiety.",
                 edu="Taught in leadership and organizational psychology programmes.",
                 com="Helps groups see scapegoating and dependency."),
    ideas=[("basic assumption", "Bion's term for an unspoken belief that takes over a group, like dependence on a leader."),
           ("social defence", "A structure or routine that protects people from anxiety, often at the cost of the task."),
           ("role", "The part a person takes up in a system, separate from who they are."),
           ("authority", "The right to act, given by the system and taken up by the person."),
           ("primary task", "The task an organization must perform to survive.")])

D["ai"] = dict(
    explainer=["Appreciative Inquiry starts change from what already works. Instead of diagnosing problems, people interview "
               "each other about high points and strengths, then build a picture of the future from them.",
               "David Cooperrider and Suresh Srivastva developed it in the 1980s at Case Western Reserve University. It usually "
               "follows a 4-D cycle: discover, dream, design and destiny (or deliver). Summits bring a whole system into one room, "
               "sometimes hundreds of people."],
    lens="Complexity as the stories a system tells about itself: the questions people ask shape what they notice and so what grows.",
    practice=["Pair people up to interview each other about a time the organization was at its best.",
              "Pull out the themes that made those moments possible.",
              "Write provocative propositions: bold statements of the future built from those themes.",
              "Ask who is missing from the room, and invite them for the next round."],
    sectors=dict(biz="Used in strategy, culture change and mergers.",
                 ngo="Imagine Chicago used it for city-wide conversation.",
                 health="Hospitals use it to build on what goes well in patient care.",
                 edu="Schools use appreciative interviews with pupils and parents.",
                 com="Asset-based community development shares the same starting point."),
    ideas=[("appreciative inquiry", "Change that starts by studying what already works well."),
           ("4-d cycle", "Discover, dream, design and destiny: the steps of an Appreciative Inquiry."),
           ("ai summit", "A large meeting that brings a whole system together to design its future."),
           ("strength-based", "Starting from people's strengths rather than their deficits."),
           ("generative question", "A question that opens new possibilities rather than confirming what is known.")])

D["wtr"] = dict(
    explainer=["The Work That Reconnects is a set of group practices created by Joanna Macy and colleagues. It moves through "
               "a spiral of four stages: coming from gratitude, honouring our pain for the world, seeing with new eyes, and "
               "going forth.",
               "It began in the early 1980s as despair and empowerment work, for people overwhelmed by the threat of nuclear war. "
               "The core insight is that grief and fear for the world, shared openly, are signs of connection, and can become "
               "the energy for action. Macy died in 2025; the Work That Reconnects Network carries the practice on."],
    lens="Complexity as interconnection felt in the body: our pain for the world shows we are part of a larger living system, and acknowledging it frees the energy to act.",
    practice=["Begin a gathering with what people are grateful for.",
              "Make room for people to say what they fear or grieve about the world, without rushing to fix it.",
              "Try a deep-time exercise: imagine speaking with people living 200 years from now.",
              "Close with each person naming one step they will take."],
    sectors=dict(biz="Used in some sustainability teams facing climate anxiety.",
                 ngo="Sustains activists and climate workers against burnout.",
                 health="Complements care for eco-anxiety and grief.",
                 edu="Used in climate education to help students act from feeling, not despair.",
                 com="Community groups host workshops after local disasters or losses."),
    ideas=[("the spiral", "The four stages of the Work That Reconnects: gratitude, honouring pain, seeing with new eyes, going forth."),
           ("active hope", "Hope as something you do, not something you have."),
           ("deep time", "Imagining across many generations to widen your sense of the present."),
           ("the great turning", "Macy's name for the shift from an industrial growth society to a life-sustaining one."),
           ("deep ecology", "The view that all living things have value in themselves, not only for human use.")])

D["soma"] = dict(
    explainer=["Somatic practice treats the body as where change happens. Under stress, bodies narrow what people can perceive "
               "and react from old patterns. Practices that build awareness of breath, posture and sensation help people settle "
               "and act with more choice.",
               "Social justice somatics, developed by Staci Haines and generative somatics, links personal trauma to social "
               "conditions. Resmaa Menakem's cultural somatics looks at how racialized trauma lives in bodies across generations. "
               "For complex work, a settled body is a condition for listening and acting together."],
    lens="Complexity lived in the body: history and stress shape what people can perceive, so the capacity to work with complexity depends on bodies that can settle.",
    practice=["Before a hard conversation, take a minute to feel your feet and lengthen your breath.",
              "Notice where in your body you feel pressure in a meeting, and what you do next.",
              "Practise a centring exercise daily for a month, from Strozzi or generative somatics.",
              "In a group, pause and ask how people are, physically, before deciding."],
    sectors=dict(biz="Somatic leadership coaching from the Strozzi Institute.",
                 ngo="Movement organizations use generative somatics to sustain organizers.",
                 health="Trauma-informed care pays attention to the body's responses to stress.",
                 edu="Regulation practices in classrooms help students learn.",
                 com="Community healing circles address collective trauma."),
    ideas=[("somatics", "Practices that work with the body as lived from the inside."),
           ("centring", "Bringing attention back to the body to act from choice rather than reaction."),
           ("regulation", "The nervous system settling after stress so a person can think and connect."),
           ("embodiment", "How experience and history live in the body and shape action."),
           ("cultural somatics", "Menakem's approach to how racialized trauma is carried in bodies across generations.")])

# ================================================================ Change and power
D["moves"] = dict(
    explainer=["This pathway is about how social change grows from small relationships and practices rather than from a "
               "master plan. adrienne maree brown's Emergent Strategy draws on Octavia Butler and Grace Lee Boggs: change "
               "spreads like patterns in nature, through many small, adaptive actions.",
               "Margaret Wheatley and the Berkana Institute's Two Loops model describes how, as an old system declines, people "
               "build the new one in networks that connect, grow into communities of practice and finally become the new norm. "
               "How you work locally is the strategy."],
    practice=["Pick one small practice you want to see in the world and make it how your group works now.",
              "Map the people pioneering the new and connect two of them who have not met.",
              "Name who is hospicing the old system and how you can support them too.",
              "Review your group's work by asking what grew, not just what was achieved."],
    sectors=dict(biz="Purpose-driven firms borrow emergent strategy for culture change.",
                 ngo="Networks and alliances use the Two Loops model to plan transitions.",
                 health="Patient movements show change growing from small groups.",
                 edu="Student-led movements spread through relationships.",
                 com="Mutual aid networks are emergent strategy in practice."),
    ideas=[("emergent strategy", "adrienne maree brown's approach: change grows from small, adaptive, relational actions."),
           ("two loops", "Berkana's model of an old system declining while a new one grows through networks."),
           ("fractal", "The idea that how we work at small scale repeats at large scale."),
           ("network", "Connections between people who share an interest, the first stage of emergence."),
           ("community of practice", "A group that shares a practice and learns from each other over time.")])

D["host"] = dict(
    explainer=["Hosting is the craft of convening groups so that they can think and act well together. It brings a family of "
               "methods: Open Space, where participants set the agenda; World Café, small rotating table conversations; Circle; "
               "and Liberating Structures, 33 simple patterns that replace the usual meeting formats.",
               "The Art of Hosting community teaches these as a practice, not a toolkit. The host's job is to set a clear purpose, "
               "invite the right people and create conditions for the conversation that matters, then trust the group."],
    lens="Complexity in the room: when the right people meet around a real question, the group can produce ideas and commitments no one brought with them.",
    practice=["Write a powerful question for your next meeting, one people actually want to talk about.",
              "Replace one presentation with a 1-2-4-All from Liberating Structures.",
              "Try Open Space for an issue with many owners: let participants set the agenda.",
              "Close with a harvest: decide how the group's thinking will be captured and used."],
    sectors=dict(biz="Liberating Structures are widely used in agile teams.",
                 ngo="Art of Hosting is common in networks and coalitions.",
                 health="World Café and Open Space are used in health service redesign.",
                 edu="Teachers use Liberating Structures in classrooms.",
                 com="Citizens' assemblies and neighbourhood meetings use these formats."),
    ideas=[("open space", "A meeting where participants set the agenda and go where they can contribute most."),
           ("world café", "Small table conversations that rotate, so ideas cross-pollinate across a large group."),
           ("liberating structures", "33 simple patterns for meetings that include everyone."),
           ("harvest", "Capturing what a gathering produced so it can be used."),
           ("powerful question", "A question that invites real thinking and matters to the people in the room.")])

D["power"] = dict(
    explainer=["Power analysis makes power visible. Steven Lukes described three faces of power: who wins in open decisions, "
               "who controls which issues ever reach the table, and how beliefs and norms make some arrangements seem natural.",
               "John Gaventa's Power Cube adds spaces (closed, invited, claimed), levels (local to global) and forms (visible, "
               "hidden, invisible). Lisa VeneKlasen and Valerie Miller turned these into practical tools for organizers. Much "
               "systems work skips power; this pathway puts it back."],
    practice=["Map a decision you care about: who decides, who sets the agenda, and which beliefs keep others out.",
              "Sort the spaces where your issue is discussed into closed, invited and claimed.",
              "Name your own position: where do you hold power, and where do you lack it?",
              "Ask who benefits from things staying as they are."],
    sectors=dict(biz="Stakeholder mapping often misses hidden and invisible power.",
                 ngo="Advocacy groups use the Power Cube to plan campaigns.",
                 health="Shows who shapes health policy and whose voices are missing.",
                 edu="Popular education uses power analysis with learners.",
                 com="Organizers map power before choosing targets."),
    ideas=[("three faces of power", "Lukes' visible, hidden and invisible power: decisions, agenda-setting and shaping beliefs."),
           ("power cube", "Gaventa's tool for analysing the spaces, levels and forms of power."),
           ("claimed space", "A space that people create for themselves, outside official channels."),
           ("invisible power", "Power that works through norms and beliefs, so people do not see it as power."),
           ("positionality", "Where you stand in relation to power, and how that shapes what you see.")])

D["narr"] = dict(
    explainer=["Narrative change works on the deep stories a society uses to make sense of an issue. If people believe poverty "
               "is about individual choices, policies that address structural causes will seem strange. Change the story, and "
               "different policies become thinkable.",
               "George Lakoff showed how frames shape reasoning. The FrameWorks Institute tests which frames help the public "
               "understand complex issues. Narrative Initiative focuses on long-term shifts carried by many voices. Marshall "
               "Ganz's public narrative helps individuals tell a story of self, us and now that moves people to act."],
    lens="Complexity as shared stories: what a society believes is possible emerges from many stories interacting, and shifting them takes many voices over years.",
    practice=["Write down the story people usually tell about your issue, and who it blames.",
              "Test two framings with people outside your sector and listen to how they respond.",
              "Tell a public narrative: your story of self, the story of us, and the story of now.",
              "Coordinate with others so many voices carry the same deeper story."],
    sectors=dict(biz="Brands shape cultural narratives, for better and worse.",
                 ngo="FrameWorks research guides how charities talk about their issues.",
                 health="Reframing ageing and mental health has shifted public understanding.",
                 edu="Media literacy helps students see frames at work.",
                 com="Community storytelling builds shared identity and agency."),
    ideas=[("framing", "How an issue is presented, which shapes how people reason about it."),
           ("deep story", "A widely held, often unspoken story people use to make sense of the world."),
           ("public narrative", "Ganz's method: story of self, story of us, story of now."),
           ("narrative power", "The ability to shape which stories are told and believed."),
           ("cultural model", "A shared mental shortcut people use to understand an issue.")])

D["conflict"] = dict(
    explainer=["Conflict transformation sees conflict as a sign that relationships and structures need to change, not just a "
               "problem to settle. John Paul Lederach argued that lasting peace needs moral imagination: seeing ourselves in a "
               "web of relationships that includes our enemies.",
               "The pathway brings together restorative justice (Howard Zehr), which focuses on repairing harm; Deep Democracy and "
               "Worldwork (Arnold and Amy Mindell), which bring minority voices into the room; and Nonviolent Communication "
               "(Marshall Rosenberg), which helps people hear the needs behind positions."],
    lens="Complexity as conflict carrying information: tensions show where a system's relationships and structures are out of step, and working through them can change the whole.",
    practice=["Before mediating, ask what relationships need to change, not only what deal is possible.",
              "In a restorative circle, ask: what happened, who was affected, and what is needed to repair it?",
              "Listen for the need behind a position and say it back.",
              "In a group decision, ask whether any minority view has not been heard yet."],
    sectors=dict(biz="Workplace mediation and restorative approaches to grievances.",
                 ngo="Peacebuilding organizations work at community and national scale.",
                 health="Restorative approaches after clinical harm support patients and staff.",
                 edu="Restorative practice in schools reduces exclusions.",
                 com="Community mediation and circles address neighbour disputes."),
    ideas=[("moral imagination", "Lederach's capacity to see a web of relationships that includes adversaries."),
           ("restorative justice", "Responding to harm by repairing it, with those affected involved."),
           ("deep democracy", "The Mindells' practice of bringing all voices, including marginal ones, into awareness."),
           ("nonviolent communication", "Rosenberg's method of naming observations, feelings, needs and requests."),
           ("conflict transformation", "Working with conflict to change relationships and structures, not just to settle it.")])

D["crisis"] = dict(
    explainer=["This pathway draws on research into what really happens when disaster strikes. Contrary to the image of panic, "
               "people usually help each other: Rebecca Solnit calls the communities that form a paradise built in hell. Daniel "
               "Aldrich showed that social ties predict recovery better than money.",
               "High reliability organizations, like aircraft carriers and nuclear plants, stay safe by staying alert to small "
               "failures and letting the person with the most relevant knowledge decide. Mutual aid, which Dean Spade describes, "
               "is how communities organize to meet needs directly."],
    practice=["Map who knows whom on your street before an emergency, and who might need help.",
              "Run a short after-action review after any incident: what happened, why, and what we will change.",
              "Practise deferring to expertise: in a crisis, who in the room knows most about this?",
              "Plan to work with spontaneous volunteers rather than turning them away."],
    sectors=dict(biz="High reliability practices in aviation, energy and manufacturing.",
                 ngo="Humanitarian groups increasingly back local mutual aid.",
                 health="Hospitals adopt high reliability principles to reduce harm.",
                 edu="Schools plan for emergencies with community ties in mind.",
                 com="Mutual aid networks formed widely during the COVID-19 pandemic."),
    ideas=[("high reliability organization", "An organization that operates safely in high-risk conditions by staying alert to small failures."),
           ("mutual aid", "People meeting each other's needs directly, as equals, outside formal charity."),
           ("social capital", "The networks and trust that let people act together."),
           ("preoccupation with failure", "Treating small errors as signs of bigger risks."),
           ("deference to expertise", "Letting whoever knows most about the situation make the call.")])

D["ritual"] = dict(
    explainer=["Every real transition passes through an in-between time, when old roles have ended and new ones have not "
               "formed. Arnold van Gennep described rites of passage in three phases: separation, the threshold, and "
               "return. Victor Turner called the threshold liminality, and the bond people form there communitas.",
               "William Bridges applied this to organizations: change is the external event, but transition is the inner "
               "process of letting go, the neutral zone, and new beginnings. Francis Weller writes about grief as communal work. "
               "Systems change involves endings, and ritual helps people through them."],
    lens="Complexity as threshold: systems change passes through an unstable in-between time, and how people are held there shapes what emerges.",
    practice=["When something ends, mark it: name what is being lost and thank it.",
              "Tell people in a reorganization that a confusing middle period is normal.",
              "Hold a simple ritual for a team ending or a programme closing.",
              "Make space for grief in community after a loss."],
    sectors=dict(biz="Bridges' transition model is used in change management.",
                 ngo="Charities closing programmes use endings rituals with staff and partners.",
                 health="Hospice and bereavement care hold people through the most personal transitions.",
                 edu="Graduations and orientation are rites of passage that can be designed with care.",
                 com="Grief rituals and memorials help communities after disasters."),
    ideas=[("liminality", "The in-between state of a transition, when old roles are gone and new ones have not formed."),
           ("rite of passage", "A ritual marking a transition, with separation, threshold and return."),
           ("communitas", "The strong bond among people going through a threshold together."),
           ("neutral zone", "Bridges' term for the confusing middle of a transition."),
           ("communal grief", "Grieving together as a community, as Weller describes.")])

# ================================================================ Practice and learning
D["dthink"] = dict(
    explainer=["Design thinking is a way of solving problems that starts with people. Teams observe and interview users, "
               "frame the problem, generate ideas, build quick prototypes and test them, going round the loop several times.",
               "It was popularized by IDEO and the Stanford d.school, building on design research by Herbert Simon, Horst Rittel "
               "and Nigel Cross. It works well for bounded problems. Critics, like Natasha Iskander, note that it can keep power "
               "with designers and miss systemic causes."],
    lens="Complexity met by making: you understand a problem better by building rough versions and watching what people do with them.",
    practice=["Watch three people use the thing you want to improve, without helping.",
              "Write the problem as a question starting with 'How might we'.",
              "Build a rough prototype in an afternoon and test it the next day.",
              "Ask who is not in the design process who should be."],
    sectors=dict(biz="Product and service development in many firms.",
                 ngo="Human-centred design for programmes, as with the Embrace infant warmer.",
                 health="Patient-centred redesign of clinics and devices.",
                 edu="Design thinking courses at d.schools worldwide.",
                 com="Community makers and civic tech groups prototype local fixes."),
    ideas=[("human-centred design", "Design that starts from the needs and behaviour of the people who will use it."),
           ("prototype", "A rough version of an idea, made to learn quickly."),
           ("how might we", "A question format that turns a problem into an invitation to ideas."),
           ("empathy", "In design thinking, understanding users by watching and listening closely."),
           ("iteration", "Repeating the build-test-learn cycle to improve.")])

D["svc"] = dict(
    explainer=["Service design looks at a service the way the person using it experiences it: as one journey from first need "
               "to final outcome, across websites, letters, phone calls, counters and waiting rooms. It then designs the "
               "frontstage (what people see) and the backstage (the staff, systems and rules behind it) together.",
               "Lynn Shostack introduced the service blueprint in 1984. The UK's Government Digital Service made it central to "
               "public services, and Lou Downe set out plain principles for good services. Done well, it exposes the policy "
               "and system problems hiding behind a bad experience."],
    lens="Complexity in the journey: a service is many systems meeting one person, and the experience emerges from how front and back stages connect.",
    practice=["Follow one person through a whole service, from first need to final outcome, and draw it.",
              "Make a service blueprint showing what users see and the backstage work behind each step.",
              "Test a service against Lou Downe's 15 principles of good services.",
              "Fix one handoff where users have to repeat themselves."],
    sectors=dict(biz="Banking, retail and telecoms use service design to cut friction.",
                 ngo="Charities redesign advice and support services around users.",
                 health="Patient journeys through hospitals and GP surgeries.",
                 edu="Student services and admissions redesigned end to end.",
                 com="Community services, such as food banks, mapped from the user's side."),
    ideas=[("service design", "Designing a service end to end: what people experience and the behind-the-scenes work that makes it happen."),
           ("service blueprint", "A diagram of a service showing what users see, and the backstage work behind each step."),
           ("journey map", "A picture of the steps someone goes through to get something done, and how each step feels."),
           ("good services", "Lou Downe's plain-language standards for what makes a service work well for the people using it."),
           ("user research", "Learning directly from the people who use a service: watching, asking, testing.")])

D["pd"] = dict(
    explainer=["Participatory design means designing with people, not for them. It began in Scandinavia in the 1970s, when "
               "trade unions and designers worked together on new workplace technology so workers had a say.",
               "Co-design (Elizabeth Sanders) and design for social innovation (Ezio Manzini) carried it forward. Design justice "
               "(Sasha Costanza-Chock) asks who benefits and who is harmed by design, and centres the people most affected. "
               "Arturo Escobar's Designs for the Pluriverse argues for many ways of living, not one."],
    lens="Complexity as many worlds: the people living with a problem hold knowledge designers lack, and good design shares power with them.",
    practice=["Invite people affected by a problem to help frame it before any ideas are generated.",
              "Pay participants for their time and expertise.",
              "Share decision power: agree which decisions participants make, not just advise on.",
              "Ask who could be harmed by the design and include them."],
    sectors=dict(biz="Co-design with customers and workers on products and tools.",
                 ngo="Design justice shapes programmes with communities.",
                 health="Co-production of services with patients and carers.",
                 edu="Co-designing learning spaces with students.",
                 com="Communities design their own spaces and services."),
    ideas=[("co-design", "Designing together with the people who will use or be affected by the result."),
           ("design justice", "Design led by marginalized communities, aiming to dismantle structural inequality."),
           ("pluriverse", "A world where many worlds fit, in Escobar's phrase from the Zapatistas."),
           ("participatory design", "Design in which users take part in decisions, rooted in Scandinavian workplace democracy."),
           ("co-production", "Public services designed and delivered with the people who use them.")])

D["trans"] = dict(
    explainer=["Transition design is design for long-term societal change, such as moving to sustainable food, energy or "
               "transport systems. It was developed at Carnegie Mellon by Terry Irwin, Gideon Kossoff, Cameron Tonkinwise and "
               "colleagues.",
               "It asks designers to map the wicked problem and its history, envision a long-horizon future, and design "
               "interventions at many levels and timescales that move the system toward it. It draws on living systems and "
               "social change theory."],
    lens="Complexity as long transition: societies change over decades through many linked shifts, so design must work across scales and timescales at once.",
    practice=["Map your problem's history: how did it come to be this way?",
              "Write a vision for 40 years ahead and work back to now.",
              "Design a small intervention today that points toward that future.",
              "Link projects at household, community and policy scale."],
    sectors=dict(biz="Firms in energy and food use it to plan long transitions.",
                 ngo="Environmental groups apply it to systemic campaigns.",
                 health="Long-term shifts toward prevention and community health.",
                 edu="Taught in design schools as an alternative to short-term projects.",
                 com="Transition Towns and local food networks share the spirit."),
    ideas=[("transition design", "Design for long-term societal transitions toward sustainable futures."),
           ("wicked problem", "A problem with no clear definition, no right answer, and no point where it is solved for good."),
           ("backcasting", "Imagining a desired future and working backward to see what steps lead there."),
           ("multi-level perspective", "A model of transitions as interactions between niches, regimes and landscapes."),
           ("long horizon", "Thinking in decades, not quarters.")])

D["labs"] = dict(
    explainer=["Strategic design uses design to change institutions: the rules, budgets, contracts and culture that shape what "
               "services can be. Policy labs inside or alongside government test new approaches with civil servants and "
               "citizens.",
               "Helsinki Design Lab and Denmark's MindLab were early examples; Policy Lab UK and France's La 27e Région followed. "
               "Dark Matter Labs works on the deep infrastructure of finance, ownership and governance. The aim is change that "
               "lasts because the system underneath it has changed."],
    lens="Complexity in the institution: services sit on top of rules, money and culture, so lasting change means redesigning that dark matter too.",
    practice=["Pick a policy problem and prototype the experience of the policy before writing it.",
              "Work with the people who write budgets and contracts, not just service teams.",
              "Run a small lab with frontline staff and residents for six weeks.",
              "Document what you learn about the institution, not just the product."],
    sectors=dict(biz="Corporate innovation labs face the same challenge of changing the host.",
                 ngo="Social labs bring many organizations together on one issue.",
                 health="Health innovation labs redesign pathways and commissioning.",
                 edu="Education labs test new models with schools and ministries.",
                 com="Civic labs give residents a role in testing policy."),
    ideas=[("policy lab", "A team that brings design and experimentation into policymaking."),
           ("strategic design", "Using design to change institutions and the conditions around services."),
           ("dark matter", "Dan Hill's term for the hidden rules, culture and money that shape what institutions can do."),
           ("prototype", "A rough version of an idea, made to learn quickly."),
           ("stewardship", "Looking after the health of a whole system rather than controlling its parts.")])

D["improve"] = dict(
    explainer=["Improvement treats an organization as a system to be improved continually through small cycles of learning. "
               "W. Edwards Deming taught that most problems come from the system, not the people, and that leaders must understand "
               "variation and learn through Plan-Do-Study-Act cycles.",
               "Toyota and Lean built this into daily work. In health care, Don Berwick and the Institute for Healthcare "
               "Improvement spread PDSA cycles widely. Agile software development shares the idea: deliver small, learn, adjust."],
    lens="Complexity as variation: outcomes come from systems, not individuals, so improvement means learning how the system behaves through many small tests.",
    practice=["Pick one measure and plot it over time on a run chart before reacting to any single result.",
              "Run a PDSA cycle: plan a small change, try it, study the result, act on what you learned.",
              "Ask the people doing the work what gets in their way.",
              "Stop blaming individuals for problems the system produces."],
    sectors=dict(biz="Lean and Toyota Production System in manufacturing and services.",
                 ngo="Quality improvement in programme delivery.",
                 health="IHI and the 100,000 Lives Campaign.",
                 edu="Improvement science in schools through networked improvement communities.",
                 com="Small tests of change in community projects."),
    ideas=[("pdsa", "Plan-Do-Study-Act: a small cycle of testing a change and learning from it."),
           ("system of profound knowledge", "Deming's four parts: systems, variation, knowledge and psychology."),
           ("variation", "The natural ups and downs in any measure; telling noise from signal."),
           ("lean", "A way of working that removes waste and improves flow."),
           ("run chart", "A graph of a measure over time, to see real change.")])

D["deval"] = dict(
    explainer=["Developmental evaluation supports innovation in complex settings. Instead of judging a programme at the end, "
               "the evaluator works alongside the team, feeding back what is happening so the programme can adapt.",
               "Michael Quinn Patton developed it for situations where the goal and the path are still emerging. Mark Cabaj and "
               "the Tamarack Institute spread it in community change work. It asks: what are we learning, and what should we do "
               "next?"],
    lens="Complexity as emergent results: when goals and paths are still forming, evaluation must learn alongside the work, not judge it afterward.",
    practice=["Bring an evaluator into the team from the start, not at the end.",
              "Agree a few learning questions and review them every month or two.",
              "Track what changed in the strategy and why.",
              "Report to funders what was learned, including what did not work."],
    sectors=dict(biz="Used in social innovation units and impact investing.",
                 ngo="Community change initiatives use it to adapt as they go.",
                 health="Evaluating new models of care while they are still forming.",
                 edu="Evaluating school reform while it unfolds.",
                 com="Community-led projects use it to learn together."),
    ideas=[("developmental evaluation", "Evaluation that supports a programme to adapt while it runs."),
           ("learning question", "A question a team agrees to explore together over time."),
           ("emergent strategy", "A strategy that takes shape through action and learning."),
           ("utilization-focused evaluation", "Patton's principle that evaluation should be useful to its intended users."),
           ("summative evaluation", "Evaluation that judges results at the end, which developmental evaluation is not.")])

D["ar"] = dict(
    explainer=["Action research combines research and change into one process. People affected by a problem study it together, "
               "act, look at what happened, and act again. Kurt Lewin coined the term in the 1940s.",
               "Paulo Freire and Orlando Fals-Borda developed participatory action research with communities in Latin America, "
               "treating them as researchers of their own lives. Peter Reason and Hilary Bradbury brought the many traditions "
               "together. Knowledge and power are shared."],
    lens="Complexity known from inside: the people in a situation understand it best by changing it and reflecting together.",
    practice=["Gather people affected by a problem and agree a shared question.",
              "Plan a small action, take it, and meet to reflect on what happened.",
              "Repeat the cycle several times, writing down what you learn.",
              "Share findings back with the community first, in a form they can use."],
    sectors=dict(biz="Action learning and action science in organizations.",
                 ngo="Participatory research with communities served.",
                 health="Patient-led research and participatory health research.",
                 edu="Teacher action research in classrooms.",
                 com="Communities research their own housing, health and environment."),
    ideas=[("action research", "Research and change as one cycle, done with the people affected."),
           ("participatory action research", "Action research led by communities, linking knowledge to power."),
           ("co-research", "Research where participants are researchers too."),
           ("cycle of inquiry", "Plan, act, observe, reflect, and repeat."),
           ("praxis", "Action and reflection together, in Freire's sense.")])

D["posdev"] = dict(
    explainer=["Positive deviance starts from a simple observation: in almost every community, a few people facing the same "
               "problem do better than others, with no extra resources. Finding out what they do differently, and helping it "
               "spread, is often faster than importing outside solutions.",
               "Jerry and Monique Sternin developed it with Save the Children in Vietnam in the 1990s, where some poor families "
               "had well-nourished children. The method has since been used in health care, education and business."],
    lens="Complexity as local solutions already present: the answer to a complex problem often exists in the system, practised by a few, waiting to be noticed.",
    practice=["Define the problem with the community, then find those who succeed against the odds.",
              "Learn what they do differently by watching, not just asking.",
              "Let the community design ways to practise those behaviours, rather than telling them.",
              "Track progress with the community."],
    sectors=dict(biz="Finding high-performing teams and spreading their practices.",
                 ngo="Nutrition and health programmes in many countries.",
                 health="Hospital infection control, through the Plexus Institute's work.",
                 edu="Finding teachers whose students thrive and learning from them.",
                 com="Communities discovering their own solutions."),
    ideas=[("positive deviance", "People who succeed against the odds, with the same resources as others."),
           ("bright spots", "Places where something is already working."),
           ("acting your way into thinking", "PD's principle that people change by practising, not by being told."),
           ("community ownership", "The community leads, discovers and spreads the solution."),
           ("uncommon practice", "A behaviour that explains why a few do better.")])

D["exp"] = dict(
    explainer=["Experiential learning describes learning as a cycle: you have an experience, reflect on it, make sense of it, "
               "and try something new. David Kolb's cycle built on John Dewey and Kurt Lewin.",
               "Donald Schön added reflection-in-action: skilled practitioners think while they work, adjusting as surprises "
               "come up. Complexity is mostly learned this way, by acting and reflecting, because no rulebook covers it."],
    lens="Complexity of practice: real situations do not match the textbook, so learning happens by acting, noticing and adjusting.",
    practice=["After any significant piece of work, write three lines: what happened, what I noticed, what I will try next.",
              "Pair up for reflective supervision once a month.",
              "Notice a surprise during your work and ask what it tells you.",
              "Build learning reviews into the end of each project."],
    sectors=dict(biz="Action learning and on-the-job development programmes.",
                 ngo="Reflective practice for frontline workers.",
                 health="Reflective supervision for clinicians and social workers.",
                 edu="Outdoor and experiential education, like Outward Bound.",
                 com="Community learning through doing projects together."),
    ideas=[("experiential learning cycle", "Kolb's cycle: experience, reflection, conceptualization, experimentation."),
           ("reflection-in-action", "Schön's idea of thinking on your feet as you work."),
           ("reflective practice", "Regularly looking back at your work to learn from it."),
           ("double-loop learning", "Argyris and Schön's idea of questioning the assumptions behind your actions, not just the actions."),
           ("learning by doing", "Dewey's principle that we learn through experience.")])

D["transl"] = dict(
    explainer=["Transformative learning is learning that changes how you see, not just what you know. Jack Mezirow found that "
               "it often starts with a disorienting dilemma, a situation your current assumptions cannot explain, and moves "
               "through critical reflection to a new perspective.",
               "Others, like Edward Taylor and Patricia Cranton, broadened the theory. Threshold concepts (Jan Meyer and Ray Land) "
               "name the ideas in a field that are troublesome at first but transform understanding once grasped."],
    lens="Complexity of mind: some learning changes the frame through which everything else is seen, and that change is often uncomfortable before it is freeing.",
    practice=["Notice a moment when something did not fit your assumptions, and write about what it challenged.",
              "Ask a group what they assumed before a project and what they assume now.",
              "In teaching, identify the threshold concepts learners find troublesome and give them time there.",
              "Make space for discomfort; do not rush to resolve it."],
    sectors=dict(biz="Leadership development aimed at shifting mindsets.",
                 ngo="Training that asks staff to rethink assumptions about the people they serve.",
                 health="Professional education where clinicians question their frames.",
                 edu="Threshold concepts guide curriculum design in universities.",
                 com="Community education that shifts how people see their situation."),
    ideas=[("disorienting dilemma", "A situation that your current assumptions cannot explain, which can trigger transformation."),
           ("perspective transformation", "Mezirow's term for a change in the frame through which you see the world."),
           ("threshold concept", "An idea that is troublesome to learn but transforms understanding once grasped."),
           ("critical reflection", "Examining the assumptions behind your beliefs."),
           ("troublesome knowledge", "Knowledge that feels strange or counter-intuitive at first.")])

D["popedu"] = dict(
    explainer=["Critical and popular education treats learning as a practice of freedom. Paulo Freire taught adult literacy "
               "in Brazil by starting from learners' own words and lives, so that reading the word became reading the world. "
               "He called the awakening of critical awareness conscientization.",
               "Myles Horton's Highlander Folk School trained labour and civil rights leaders, including Rosa Parks. bell hooks "
               "wrote about engaged pedagogy that honours students as whole people. The thread: education that helps people "
               "name and change the forces shaping their lives."],
    lens="Complexity as lived and named: people understand the systems around them best when they analyse them from their own experience and act together.",
    practice=["Start a session with participants' experience of the issue, not with expert input.",
              "Use a code, such as a picture or a story, that people can analyse together.",
              "Ask: why is it this way, who benefits, and what can we do?",
              "Turn learning into action the group chooses."],
    sectors=dict(biz="Worker education and union learning.",
                 ngo="Community organizations use popular education to build leadership.",
                 health="Popular education in community health worker programmes.",
                 edu="Critical pedagogy in schools and universities.",
                 com="Highlander and similar schools train community leaders."),
    ideas=[("conscientization", "Freire's term for developing critical awareness of the forces shaping your life."),
           ("banking model", "Freire's critique of education that deposits facts into passive learners."),
           ("praxis", "Action and reflection together, in Freire's sense."),
           ("engaged pedagogy", "bell hooks' teaching that honours students as whole people."),
           ("popular education", "Education rooted in people's experience, aimed at social change.")])

D["cop"] = dict(
    explainer=["Communities of practice are groups of people who share a concern or a craft and learn from each other over "
               "time. Jean Lave and Etienne Wenger studied how apprentices learn by taking part in such communities.",
               "Action learning, created by Reg Revans, brings small groups together to work on real problems by asking each "
               "other questions rather than giving advice. Etienne and Beverly Wenger-Trayner extended these ideas to social "
               "learning across whole systems."],
    lens="Complexity as learning held in groups: knowledge about complex work lives in people's practice, and spreads through relationships over time.",
    practice=["Find five to ten people who share your practice and meet monthly.",
              "Bring a real problem to an action learning set and only receive questions for the first half hour.",
              "Keep a shared log of stories and lessons.",
              "Invite newcomers to take part at the edge and grow toward the centre."],
    sectors=dict(biz="Communities of practice spread know-how across large firms.",
                 ngo="Peer networks share learning across charities.",
                 health="Clinical communities of practice improve care.",
                 edu="Teacher learning communities and professional networks.",
                 com="Practitioner networks across neighbourhoods and cities."),
    ideas=[("community of practice", "A group that shares a practice and learns from each other over time."),
           ("action learning", "Revans' method: small groups work on real problems through questions."),
           ("legitimate peripheral participation", "Lave and Wenger's idea that newcomers learn by taking part at the edge."),
           ("social learning", "Learning that happens through relationships and shared practice."),
           ("systems convening", "Wenger-Trayner's term for bringing people together across boundaries to learn.")])

D["adult"] = dict(
    explainer=["Adult development research suggests that adults can keep growing in how they make sense of the world, becoming "
               "more able to hold several perspectives, uncertainty and contradiction. Robert Kegan described a series of such "
               "shifts in In Over Our Heads.",
               "Kegan and Lisa Lahey's immunity to change explains why people stay stuck: hidden competing commitments protect "
               "them from something they fear. Jennifer Garvey Berger made these ideas practical for leaders in complexity. "
               "Critics, including Nora Bateson, warn against ranking people by stage."],
    lens="Complexity of mind: the capacity to hold complexity grows over a lifetime, and stuck change often hides a commitment worth understanding.",
    practice=["Map your own immunity to change: goal, what you do instead, hidden worries, big assumptions.",
              "Test one big assumption with a small, safe experiment.",
              "Ask a colleague how they see a problem and try to describe it in their terms.",
              "Avoid using stages to label people; use them to ask what support someone needs."],
    sectors=dict(biz="Leadership programmes and deliberately developmental organizations.",
                 ngo="Supports leaders facing complex, uncertain work.",
                 health="Coaching for clinicians moving into leadership.",
                 edu="Adult education and teacher development.",
                 com="Peer coaching in community leadership."),
    ideas=[("immunity to change", "Kegan and Lahey's term for hidden commitments that keep us from changing."),
           ("subject-object shift", "Kegan's idea that growth means being able to look at what you used to look through."),
           ("big assumption", "A belief taken as true that holds an immunity to change in place."),
           ("vertical development", "Growth in how you make sense of the world, not just in skills."),
           ("self-authoring mind", "Kegan's stage where people form their own values rather than following others'.")])

D["cxedu"] = dict(
    explainer=["This pathway asks what education looks like when we take complexity seriously: classrooms, schools and learning "
               "systems are complex systems themselves, and learners face a world no one can predict.",
               "Edgar Morin's Seven Complex Lessons, written for UNESCO, argued that education must teach the human condition, "
               "uncertainty and understanding. Brent Davis and Dennis Sumara applied complexity science to teaching. The Inner "
               "Development Goals offer a framework of inner capacities for working on global challenges."],
    lens="Complexity of learning: learning emerges from relationships between learners, teachers and context, and preparing people for an unpredictable world means teaching uncertainty, not only answers.",
    practice=["Design one lesson around an open question with no single right answer.",
              "Let students explore a local system, like the school's food or energy, as a complex system.",
              "Assess learning by how students handle uncertainty, not only by recall.",
              "Treat the school itself as a learning system: what feedback loops help it improve?"],
    sectors=dict(biz="Corporate learning moving toward capacities, not just skills.",
                 ngo="Education charities designing for adaptability.",
                 health="Training clinicians to work with uncertainty.",
                 edu="Home ground: schools, universities and learning designers.",
                 com="Community learning that builds collective capacity."),
    ideas=[("complexity thinking", "Seeing a situation as many interacting parts producing patterns no one part explains."),
           ("inner development goals", "A framework of inner capacities, like perspective-taking and self-awareness, for working on global challenges."),
           ("emergence", "When a whole shows patterns that none of its parts have on their own."),
           ("teaching uncertainty", "Morin's call to prepare learners for the unexpected."),
           ("learning system", "An organization or community designed to learn continually.")])
