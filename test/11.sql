SELECT h_mainkey
FROM hand, mainCards
WHERE
h_mainkey = m_mainkey AND
h_playerkey = key AND
m_effect LIKE “%Play this card during scoring%”
