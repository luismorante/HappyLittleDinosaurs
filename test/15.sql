SELECT h_mainkey
FROM hand, mainCards
WHERE
h_playerkey = key AND
m_effect LIKE “%Play this card if you would add a Disaster card to your Disaster Area this round.%”
