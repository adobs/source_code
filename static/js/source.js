
$(function() {

    function displayTagCount(data){
        $("#tag-count-header").show();
        $("#tag-count-loading").hide();

        // iterate through the object of tags and counts
        $.each( data, function( key, value ) {
          $("#tag-count").append( "<a class='source-text-link' name="+key+">"+key+"</a>" + ": " + value+" time(s)<br>" );
        });
    }

    function displaySourceText(data){
        $("#source-text-header").show();
        $("#source-text-loading").hide();
        $("#source-text").html(data);
        $("#submit-btn").removeAttr("disabled");

    }

    function executeSearch(evt){
        var url = {
            "source": $("#source").val()
        };

        // AJAX calls - fill in tag counts and source text of URL
        $.get("/count-tags.json", url, displayTagCount);
        $.get("/source-text.json", url, displaySourceText);

        //get rid of previous content
        $("#tag-count").empty();
        $("#source-text").empty();
        
        // loading wheels in each section
        $("#tag-count-loading").show();
        $("#source-text-loading").show();
        $("#tag").show();

        // disable button
        $("#submit-btn").prop("disabled", "true");
    }

    // event listener for URL submission
    $("#input-form").on("submit", executeSearch);

    $(".source-text-link").on("click", function(){
        console.log("HERE");
        $("div").unhighlight();
        var tag = $(this).attr("name");
        console.log("tag is "+ tag);
        $("div").highlight(tag);
    });
    

});
