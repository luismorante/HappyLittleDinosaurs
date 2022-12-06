SELECT m_name
FROM mainCards, hand
WHERE
h_mainkey = m_mainkey AND
h_playerkey = key
