html_header = """
<!DOCTYPE html>
    <html>
    <title> Rainbow Six Siege Op.GG Copy </Title>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    * {
      box-sizing: border-box;
      text-align: center;
    }

    /* Create two equal columns that floats next to each other */
    .column {
      float: left;
      width: 30%;
      padding: 10px;
      height: 300px; /* Should be removed. Only for demonstration */
    }

    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        height: 80px;
        width: 80px;
    }

    p {
        margin-left: auto;
        margin-right: auto;
        width: 4em;
        
    }
    
    .winrate {
        text-align: center;
    }

    /* Clear floats after the columns */
    .row:after {
      content: "";
      display: table;
      clear: both;
    }
    </style>
    </head>
    <div class="row">
      <div class="column">
      """

HTML_win = '<div class="trn-defstat__name">Win %</div>'


url = "C:\\Users\\Nirav\\PycharmProjects\\RainbowScriptUpdate\\helloworld.html"