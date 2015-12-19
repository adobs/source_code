// todo
// questions
// why does function highlight need to be outside of the on ready?

    function highlight(evt){
        var tag = $(evt.target).prop("name");
        $("div#source-text").unhighlight();

        // highlight a beginning tag
        $("div#source-text").highlight("<"+tag);

        // highlight an ending tag
        $("div#source-text").highlight("</"+tag+">");

        $("#tag-info").empty();
        $("#tag-info").html("<span id='yellow'>"+tag+"</span> tag is highlighted");
    }

$(function() {


    function displayTagCount(data){
        $("#tag-count-header").show();
        $("#tag-count-loading").hide();

        // iterate through the object of tags and counts
        $.each( data, function( key, value ) {
          $("#tag-count").append( "<a class='source-text-link' onclick='highlight(event)' name="+key+">"+key +"</a>"+ ": " + value+" time(s)<br>" );
        });
    }

    function displaySourceText(data){
        $("#source-text-header").show();
        $("#source-text-loading").hide();
        $("#source-text").html(data);
        $("#submit-btn").removeAttr("disabled");

        // show TOP buttom (at bottom of source text)
        $("#top-btn").show();
    }

    function executeSearch(evt){
        evt.preventDefault();

            var url = {
            "source": $("#source").val()
        };

        // AJAX calls - fill in tag counts and source text of URL
        $.get("/count-tags.json", url, displayTagCount);
        $.get("/source-text.json", url, displaySourceText);

        // get rid of previous content
        $("#tag-count").empty();
        $("#source-text").empty();
        
        // loading wheels in each section
        $("#tag-count-loading").show();
        $("#source-text-loading").show();

        // disable button
        $("#submit-btn").prop("disabled", "true");

        $("#tag").show();   

        // scroll 
        window.location = "#tag";


    }

    // event listener for URL submission
    $("#input-form").on("submit", executeSearch);
    

});
