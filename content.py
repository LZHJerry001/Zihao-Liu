"""Content for Zihao Liu's academic website. Update the lists below and run build.py."""

CV = 'https://drive.google.com/file/d/1dbuDF9y7nq0dY5gd0Cb7Kib8wQsK6FTQ/view?usp=drive_link'
PAPER_RAAG = 'https://arxiv.org/abs/2609.21946'
PAPER_ENTROPY = 'https://www.ams.org/journals/bproc/2023-10-25/S2330-1511-2023-00182-8/S2330-1511-2023-00182-8.pdf'
SLIDES = 'https://drive.google.com/file/d/10Yw78RKarLAzLN6q5c4R68Xe2iyZyS72/view?usp=drive_link'
COURSE = 'https://sites.google.com/view/math212fall2024/home'

papers = [
    {'title': 'Finite quotients of right-angled Artin groups', 'authors': 'Zihao Liu', 'publication': 'Preprint · arXiv:2609.21946 (2026)', 'url': PAPER_RAAG, 'link': 'View on arXiv'},
    {'title': 'Scaled homology and topological entropy', 'authors': 'Bingzhe Hou, Kiyoshi Igusa, and Zihao Liu', 'publication': 'Proceedings of the American Mathematical Society, Series B 10 (2023), 273–287', 'url': PAPER_ENTROPY, 'link': 'Read the paper'},
]

talks = [
    ('November 2026', 'Michigan State Topology Seminar', 'Finite quotients of right-angled Artin groups', None),
    ('September 2026', 'Rutgers Geometry & Topology Seminar', 'Finite quotients of right-angled Artin groups', None),
    ('June 2026', 'Beijing International Center for Mathematical Research Topology Seminar', 'Introduction to Veech groups: genus two, Teichmüller curves, and symplectic images', None),
    ('November 2024', 'SIMIS Geometry & Topology Seminar', 'Scaled homology and topological entropy', SLIDES),
    ('November 2024', 'UCR Geometry & Topology Seminar', 'Scaled homology and topological entropy', None),
    ('May 2024', 'Temple Graduate Student Conference in Algebra, Geometry, and Topology', 'Profinite rigidity', None),
    ('2024', 'Graduate Student Topology and Geometry Conference', 'Scaled homology and topological entropy', None),
    ('', 'Riverside Workshop on Geometric Group Theory: January follow-up', 'From braid groups to Artin groups', None),
    ('', 'Binghamton University Graduate Combinatorics, Algebra, and Topology Conference', 'Large scale homology', None),
    ('', 'Rice Topology Seminar', 'Scaled homology and topological entropy', None),
    ('', 'Texas A&M Graduate Student Concentration Week on Metric Geometry', 'Scaled homology and topological entropy', None),
    ('', 'Temple Graduate Student Conference in Algebra, Geometry, and Topology', 'Large scale homology', None),
    ('', 'Brandeis Topology Seminar', 'Scaled homology and topological entropy', None),
]

conferences = {
  '2026': [
    ('July', 'Vanderbilt colloquium series on groups, geometry, and dynamics', 'Vanderbilt University'),
    ('July', 'Shanghai Geometric Group Theory Workshop', 'Fudan University'),
    ('June', 'Young Geometric Group Theory XIV', 'Korea Institute for Advanced Study, Seoul'),
    ('June', 'Group Actions and Dynamics', 'The CUNY Graduate Center'),
    ('May', 'Cornell Topology Festival', 'Cornell University'),
    ('April', '2026 Bloomington Geometry Workshop', 'Indiana University, Bloomington'),
    ('January', 'Topological and Geometric Structures in Low Dimensions & Geometry and Dynamics for Discrete Subgroups of Higher Rank Lie Groups', 'Simons Laufer Mathematical Sciences Institute'),
  ],
  '2025': [
    ('December', 'Workshop on hyperbolic geometry and geometric group theory', 'SIMIS'),
    ('October', 'Computational problems about 3-manifolds, associated groups and varieties', 'Rutgers University'),
    ('June', 'The William Rowan Hamilton Geometry and Topology Workshop', 'Trinity College Dublin'),
    ('June', 'Geometric Group Theory and Related Topics', 'Beijing International Center for Mathematical Research'),
    ('May', 'Geometry and Topology of Polyhedral Complexes', 'The Ohio State University'),
    ('May', 'Recent Development in Geometric Group Theory', 'The University of Tennessee'),
    ('January', 'Hyperbolic Manifolds, Their Submanifolds and Fundamental Groups', 'IMPA'),
  ],
  '2024': [
    ('July', 'Shanghai Geometric Group Theory Workshop', 'Fudan University'),
    ('May', 'Graduate Student Conference in Algebra, Geometry, and Topology', 'Temple University'),
    ('May', 'Cornell Topology Festival', 'Cornell University'),
    ('April', 'Graduate Student Topology and Geometry Conference', 'Michigan State University'),
    ('March', 'Hot Topics: Artin Groups and Arrangements — Topology, Geometry, and Combinatorics', 'Simons Laufer Mathematical Sciences Institute'),
    ('January', 'Riverside Workshop on Geometric Group Theory: January follow-up', 'University of California, Riverside'),
  ],
  '2023': [
    ('November', 'Texas Geometry and Topology Conference', 'Rice University'),
    ('September', 'Geometry and topology of Artin groups', 'American Institute of Mathematics'),
    ('June', 'Groups around 3-Manifolds', 'Centre de Recherches Mathématiques'),
    ('June', 'Geometric Topology in New York', 'Columbia University'),
    ('May', 'Geometry of Subgroups', 'Centre de Recherches Mathématiques'),
    ('March', 'Redbud Topology Conference', 'University of Oklahoma'),
    ('March', 'Riverside Workshop on Geometric Group Theory', 'University of California, Riverside'),
  ],
  '2022': [
    ('November', 'Graduate Combinatorics, Algebra, and Topology Conference', 'Binghamton University'),
    ('August', 'Workshop on Big Mapping Class Groups', 'Boston College'),
    ('June', 'Geometry, Arithmetic, and Groups', 'University of Texas, Austin'),
    ('June', 'The Circle at Infinity', 'Harvard University'),
    ('June', '3-Manifolds, Groups, and Singularities', 'Columbia University'),
    ('May', 'Graduate Student Conference in Algebra, Geometry, and Topology', 'Temple University'),
  ],
}

instructor = [
    ('Fall 2024', 'MATH 212', 'Multivariable Calculus', 'Rice University', COURSE),
    ('Summer 2024', 'MATH 212', 'Multivariable Calculus', 'Rice University', None),
]
teaching_assistant = [
    ('Fall 2026', 'MATH 321', 'Introduction to Analysis I', 'Rice University · Instructor: Jonathan Chaika', None),
    ('Spring 2026', 'MATH 427/517', 'Complex Analysis', 'Rice University · Instructor: Francisco Arana-Herrera', None),
    ('Fall 2025', 'MATH 302', 'Elements of Analysis', 'Rice University · Instructor: Nickolas Castro', None),
    ('Spring 2025', 'MATH 365', 'Number Theory', 'Rice University · Instructor: Brandon Levin', None),
    ('Spring 2024', 'MATH 357', 'Abstract Algebra II', 'Rice University · Instructor: Stephen Wolff', None),
    ('Fall 2023', 'MATH 356', 'Abstract Algebra I', 'Rice University · Instructor: Hongdi Huang', None),
    ('Spring 2022', 'MATH 15a', 'Linear Algebra', 'Brandeis University · Instructor: Lam Pham', None),
    ('Fall 2021', 'MATH 15a', 'Linear Algebra', 'Brandeis University · Instructor: Carolyn Abbott', None),
    ('Fall 2019', 'MATH 36a', 'Probability', 'Brandeis University · Instructor: Denis Patterson', None),
]

featured_photos = [
    ('teaching-at-blackboard.jpg', 'Zihao Liu teaching at a blackboard.', 'Photo by Yuxin Yan'),
    ('zihao-at-table.jpg', 'Zihao Liu sitting at a table with friends.', 'Photo by Yiqian Wang'),
]

photos = [
    ('great-smoky-mountains.jpg', 'Great Smoky Mountains', 'Hiking in the Great Smoky Mountains.'),
    ('rainbow-falls.jpg', 'Rainbow Falls', 'With Shuxian Song, Jia Wan, and Zhihao Mu at Rainbow Falls.'),
    ('great-wall.jpg', 'The Great Wall', 'Hiking the Great Wall with Xiaolong Hans Han, Chris Leininger, and Le Kuai.'),
    ('korean-bbq.jpg', 'Korean barbecue', 'Dinner with Beibei Liu, Changqian Li, Jingyin Huang, and Zhihao Mu.'),
    ('sugarloaf-mountain.jpg', 'Sugarloaf Mountain', 'With Ricky Lee, Yi Wang, and Yushan Jiang in front of Sugarloaf Mountain.'),
]
