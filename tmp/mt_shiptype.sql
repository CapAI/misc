use ais;

# 109760 COUNT DISTINCT
select DISTINCT vessel_static.mmsi, type, url from vessel_static # , a, b, c, d, draught
	#( DISTINCT mmsi from vessel_static)
INNER JOIN scrape on vessel_static.mmsi = scrape.mmsi
INNER JOIN scrape_asset on scrape_asset.scrape_id = scrape.id
WHERE
	(url like '%jpg' OR url like '%JPEG' OR url like '%png' OR url like '%PNG')
AND
	vessel_static.mmsi REGEXP '^[2-7]'
AND
-- 	vessel_static.type = 30 # Fishing
-- 	vessel_static.type in (31,32,52) # Tug
--  vessel_static.type = 33 # Dredger
--  vessel_static.type = 34 # Dive
--  vessel_static.type = 35 # Military
--  vessel_static.type = 36 # Sailing
--  vessel_static.type = 37 # Pleasure
--  vessel_static.type = 50 # Pilot
--  vessel_static.type = 51 # Search and Rescue
--  vessel_static.type = 53 # Port Tender
--  vessel_static.type = 54 # Anti-Polution
--  vessel_static.type = 55 # Law Enforcement (Patrol)
--  vessel_static.type = 58 # Medical
-- 	vessel_static.type BETWEEN 40 AND 49 # High-speed (Hydrofoil / Hovercraft)
-- 	vessel_static.type BETWEEN 60 AND 69 # Passenger
-- 	vessel_static.type BETWEEN 70 AND 79 # Cargo
-- 	vessel_static.type BETWEEN 80 AND 89; # Tanker
-- limit 100
;


# GROUP BY vessel_static.mmsi
group by vessel_static.type;

select vessel_static.mmsi, url from vessel_static
INNER JOIN scrape on vessel_static.mmsi = scrape.mmsi
INNER JOIN scrape_asset on scrape_asset.scrape_id = scrape.id
WHERE
	vessel_static.mmsi = 538005893;
    
    
# 33: 1400  
# 35: 748  
SELECT COUNT(*) FROM
	(
SELECT DISTINCT mmsi FROM vessel_static 
	WHERE mmsi NOT IN(SELECT mmsi FROM scrape)
		AND type = 35
    ORDER BY RAND()
    ) AS tmp;
    
    
	
SELECT COUNT( DISTINCT url) from vessel_static
		INNER JOIN scrape on vessel_static.mmsi = scrape.mmsi
		INNER JOIN scrape_asset on scrape_asset.scrape_id = scrape.id
        WHERE vessel_static.type = 35
        GROUP BY vessel_static.mmsi
        ORDER BY COUNT( DISTINCT url ) DESC
        LIMIT 5;
        
        ORDER BY 