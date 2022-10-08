if( location.search.match("place")){
    select_place = location.search
    $('#place_selectbox').children('option[value="'+select_place+'"]').prop('selected', true)
    
};
if( location.search.match("day")){
    select_day = location.search
    $('#day_selectbox').children('option[value="'+select_day+'"]').prop('selected', true)
};
