# ModMapper
## John D'Alessandro

A simple python script inspired by [this post](https://www.reddit.com/r/dataisbeautiful/comments/4o15je/runcensorednews_subreddit_network_these_are_the/).

## Usage  
  The map command takes a subreddit name as an argument. Not an address, just the name, and shows how many moderators overlap with other subreddits. For example:  
       
          > map dataisbeautiful    
          Scraped 20/20 mods successfully!    
          /r/science               :  5  
          /r/dataisbeautiful       : 20  
          /r/visualization         :  2  
          /r/askscience            :  2  
          /r/personalfinance       :  2  
          /r/leagueoflegends       :  2  
          /r/ynab                  :  2  
          /r/baltimore             :  2  
          /r/rit                   :  2  
          /r/almosthomeless        :  2  
          /r/ynab4                 :  2  
  The info command takes the address of a subreddit that has already been pointed out in a map as an argument. For example:   
      
        > info /r/science  
          rhiever  
          frostickle  
          NonNonHeinous  
          AsAChemicalEngineer  
          Izawwlgood  
  The minDisplay command takes a number as an argument and sets the minimum number of moderator overlap needed to display a subreddit. The default is 2.  
