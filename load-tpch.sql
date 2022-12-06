-- .mode "table"
-- .separator "|"
-- .import data/player.tbl player

-- .mode "table"
-- .separator "|"
-- .import data/hand.tbl hand

-- .mode "table"
-- .separator "|"
-- .import data/disasterArea.tbl disasterArea

-- .mode "table"
-- .separator "|"
-- .import data/escapeRoute.tbl escapeRoute

-- .mode "table"
-- .separator "|"
-- .import data/scoring.tbl scoring

-- .mode "table"
-- .separator "|"
-- .import data/field.tbl field

-- .mode "table"
-- .separator "|"
-- .import data/upcoming.tbl upcoming

-- .mode "table"
-- .separator "|"
-- .import data/lastDisaster.tbl lastDisaster

-- .mode "table"
-- .separator "|"
-- .import data/mainCards.tbl mainCards

-- .mode "table"
-- .separator "|"
-- .import data/disasterCards.tbl disasterCards

update maincards
set m_point = 3 , m_effect = "You may discard a Point card with an effect from your hand, then add its point value to your score this round.", m_quantity = 2
where m_mainkey = 13