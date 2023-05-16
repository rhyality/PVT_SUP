WEBSITE_LIST = {"https://www.youtube.com/":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "membership":   'direct-link;signin',
                  "careers":  'css selector;ytd-rich-item-renderer'
                 },
                  "sub-endpoints":
                  {
                      "membership":{"price":'partial link text;What currency is the pricing in',
                                   },
                      "trending":{"video":'rand_ind:css selector;ytd-video-renderer'
                                  },
                      "music":{"video":'rand_ind:css selector;ytd-video-renderer'
                               },
                      "gaming":{"video":"rand_ind:css selector;ytd-video-renderer"
                    

                        
                      },
                  }
                 }
                }