from aurora.db import init_db, add_event,get_events

def test_add_and_get_events():
    con=init_db(":memory:")
    add_event(con,1,"PLAYER_HELPED",'{"npc":"maren"}')
    add_event(con,1,"PLAYER_HELPED",'{"npc":"maren"}')

    events=get_events(con)
    assert len(events)==2
    assert events[0][1]=="PLAYER_HELPED"

def test_get_events_since():
    con=init_db(":memory:")
    add_event(con,1,"A","{}")
    add_event(con,5,"B","{}")
    assert len(get_events(con,since=3))==1