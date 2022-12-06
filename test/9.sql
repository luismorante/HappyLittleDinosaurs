SELECT h_playerkey, h_mainkey
FROM hand
WHERE
h_playerkey = key AND
h_mainkey = card
