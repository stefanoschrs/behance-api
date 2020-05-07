# Behance

> Since the public API closed, there is no way to programmatically get the projects of a user.  
> This project is not meant to be deployed as a scalable, production system but rather provide an light interface for personal usage in portfolio websites etc  

### Usage
1. Server w/ Docker **(recommended)**
    ```console
    docker run --rm -p 5000:5000 stefanoschrs/behance-api
    curl localhost:5000/profile/stefanoschrs
    ```
2. Server
    ```console
    FLASK_APP=server.py flask run
    curl localhost:5000/profile/stefanoschrs
    ```
3. Directly
    ```console
    scrapy crawl behance -a username=stefanoschrs
    ```

### Interesting fields
- covers
    - original
- created_on
- description
- modules[]
    - type=text
    - text_plain
    - type=image
    - sizes.original
- name
- stats
    - views
    - appreciations
    - comments
- tags[]
    - title
- url

### Raw
```json
[
	{
		"IMAGESURL": "https://a5.behance.net/8d8d04a0a93e6463490ba5beedea7fc90083fcfe/img/",
		"agencies": [],
		"allow_comments": 1,
		"brands": [],
		"can_access": true,
		"canvas_width": 1400,
		"colors": [
			{
				"r": 28,
				"g": 34,
				"b": 60
			}
		],
		"conceived_on": 1588809600,
		"copyright": {
			"license": "cc by-nc-nd",
			"description": "Attribution-NonCommercial-NoDerivs",
			"license_id": 1,
			"label": "Attribution Non-commercial\\nNo Derivatives",
			"info": {
				"images": [
					"https://a5.behance.net/8d8d04a0a93e6463490ba5beedea7fc90083fcfe/img/project/cc/by.svg?cb=264615658",
					"https://a5.behance.net/8d8d04a0a93e6463490ba5beedea7fc90083fcfe/img/project/cc/nc.svg?cb=264615658",
					"https://a5.behance.net/8d8d04a0a93e6463490ba5beedea7fc90083fcfe/img/project/cc/nd.svg?cb=264615658"
				],
				"url": "http://creativecommons.org/licenses/by-nc-nd/4.0/deed.en_US",
				"text": "Attribution, Non-commercial, No Derivatives"
			}
		},
		"cover_scale": "0.6359192825112108",
		"cover_x": "241",
		"cover_y": "108",
		"covers": {
			"115": "https://mir-s3-cdn-cf.behance.net/projects/115/eb22a096673831.Y3JvcCw2MzUsNDk2LDM3OCwxNjk.png",
			"202": "https://mir-s3-cdn-cf.behance.net/projects/202/eb22a096673831.Y3JvcCw2MzUsNDk2LDM3OCwxNjk.png",
			"230": "https://mir-s3-cdn-cf.behance.net/projects/230/eb22a096673831.Y3JvcCw2MzUsNDk2LDM3OCwxNjk.png",
			"404": "https://mir-s3-cdn-cf.behance.net/projects/404/eb22a096673831.Y3JvcCw2MzUsNDk2LDM3OCwxNjk.png",
			"original": "https://mir-s3-cdn-cf.behance.net/projects/original/eb22a096673831.Y3JvcCw2MzUsNDk2LDM3OCwxNjk.png",
			"max_808": "https://mir-s3-cdn-cf.behance.net/projects/max_808/eb22a096673831.Y3JvcCw2MzUsNDk2LDM3OCwxNjk.png"
		},
		"created_on": 1588827896,
		"credits": [],
		"description": "Social Ads Intelligence Tool, discover the best social ads, spy on your competitors, and create winning campaigns",
		"description_shortened": null,
		"editor_version": 5,
		"featured_on": null,
		"fields": [
			{
				"id": 123,
				"name": "Programming",
				"url": "/search?field=123&content=projects"
			},
			{
				"id": 132,
				"name": "UI/UX",
				"url": "/search?field=132&content=projects"
			},
			{
				"id": 103,
				"name": "Web Development",
				"url": "/search?field=103&content=projects"
			}
		],
		"has_description": true,
		"has_multiple_owners": false,
		"has_tags": true,
		"has_teams": false,
		"has_tools": false,
		"has_tools_without_synonym": false,
		"id": 96673831,
		"is_following": null,
		"is_owner": false,
		"mature_access": "allowed",
		"mature_content": 0,
		"modified_on": 1588828272,
		"modules": [
			{
				"id": 558258299,
				"project_id": 96673831,
				"type": "text",
				"full_bleed": 0,
				"alignment": "left",
				"caption_alignment": "left",
				"is_image": false,
				"is_video": false,
				"is_embed": false,
				"is_text": true,
				"is_audio": false,
				"is_grid": false,
				"text": "<div class=\"title\"><div class=\"title\">SpyTool | Freelance</div><div class=\"sub-title\"><div><div>Social Ads Intelligence Tool, empowering you to create winning campaigns, track your competitors, and analyze trends.</div></div><div class=\"main-text\"><br></div></div><div class=\"main-text\">- Web app</div><div class=\"main-text\">- Facebook Integration</div></div><div class=\"sub-title\"><br></div><div class=\"main-text\"><div>Technologies:</div><div>- Angular</div><div>- NodeJS</div><div>- Go</div><div>- MySQL</div><div>- Linux</div></div>",
				"text_plain": "SpyTool | FreelanceSocial Ads Intelligence Tool, empowering you to create winning campaigns, track your competitors, and analyze trends.- Web app- Facebook IntegrationTechnologies:- Angular- NodeJS- Go- MySQL- Linux"
			},
			{
				"id": 558258837,
				"project_id": 96673831,
				"type": "image",
				"full_bleed": 0,
				"alignment": "center",
				"caption_alignment": "left",
				"alt_text_for_editor": "",
				"alt_text": "",
				"color": {
					"r": 254,
					"g": 254,
					"b": 254
				},
				"src": "https://mir-s3-cdn-cf.behance.net/project_modules/disp/35cf4296673831.5eb397b5143f3.png",
				"sizes": {
					"max_632": "https://mir-s3-cdn-cf.behance.net/project_modules/max_632/35cf4296673831.5eb397b5143f3.png",
					"max_316": "https://mir-s3-cdn-cf.behance.net/project_modules/max_316/35cf4296673831.5eb397b5143f3.png",
					"max_158": "https://mir-s3-cdn-cf.behance.net/project_modules/max_158/35cf4296673831.5eb397b5143f3.png",
					"disp": "https://mir-s3-cdn-cf.behance.net/project_modules/disp/35cf4296673831.5eb397b5143f3.png",
					"max_1240": "https://mir-s3-cdn-cf.behance.net/project_modules/hd/35cf4296673831.5eb397b5143f3.png",
					"max_1920": "https://mir-s3-cdn-cf.behance.net/project_modules/fs/35cf4296673831.5eb397b5143f3.png",
					"max_1200": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/35cf4296673831.5eb397b5143f3.png",
					"original": "https://mir-s3-cdn-cf.behance.net/project_modules/source/35cf4296673831.5eb397b5143f3.png"
				},
				"dimensions": {
					"max_632": {
						"width": 1290,
						"height": 632
					},
					"max_316": {
						"width": 645,
						"height": 316
					},
					"max_158": {
						"width": 323,
						"height": 158
					},
					"disp": {
						"width": 600,
						"height": 294
					},
					"max_1240": {
						"width": 1240,
						"height": 607
					},
					"max_1920": {
						"width": 1366,
						"height": 669
					},
					"max_1200": {
						"width": 1200,
						"height": 588
					},
					"original": {
						"width": 1366,
						"height": 669
					}
				},
				"is_image": true,
				"is_video": false,
				"is_embed": false,
				"is_text": false,
				"is_audio": false,
				"is_grid": false,
				"picture": {
					"sources": [
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/disp/35cf4296673831.5eb397b5143f3.png",
							"media_query": "(max-width: 633px)",
							"width": 600,
							"height": 294
						},
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/35cf4296673831.5eb397b5143f3.png",
							"media_query": "(min-width: 634px) and (max-width: 1233px)",
							"width": 1200,
							"height": 588
						},
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/fs/35cf4296673831.5eb397b5143f3.png",
							"media_query": "(min-width: 1434px) and (max-width: 1953px)",
							"width": 1366,
							"height": 669
						}
					],
					"img": {
						"src": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/35cf4296673831.5eb397b5143f3.png",
						"width": 1200,
						"height": 588
					}
				},
				"picture_largest": {
					"sources": [
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/disp/35cf4296673831.5eb397b5143f3.png",
							"media_query": "(max-width: 633px)",
							"width": 600,
							"height": 294
						},
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/35cf4296673831.5eb397b5143f3.png",
							"media_query": "(min-width: 634px) and (max-width: 1233px)",
							"width": 1200,
							"height": 588
						},
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/fs/35cf4296673831.5eb397b5143f3.png",
							"media_query": "(min-width: 1434px) and (max-width: 1953px)",
							"width": 1366,
							"height": 669
						}
					],
					"img": {
						"src": "https://mir-s3-cdn-cf.behance.net/project_modules/fs/35cf4296673831.5eb397b5143f3.png",
						"width": 1366,
						"height": 669
					}
				},
				"aspect_ratio": "49%",
				"width": 600,
				"height": 294,
				"exif": [],
				"is_lazy": false
			},
			{
				"id": 558258839,
				"project_id": 96673831,
				"type": "image",
				"full_bleed": 0,
				"alignment": "center",
				"caption_alignment": "left",
				"alt_text_for_editor": "",
				"alt_text": "",
				"color": {
					"r": 28,
					"g": 33,
					"b": 60
				},
				"src": "https://mir-s3-cdn-cf.behance.net/project_modules/disp/74442b96673831.5eb397b514b7c.png",
				"sizes": {
					"max_632": "https://mir-s3-cdn-cf.behance.net/project_modules/max_632/74442b96673831.5eb397b514b7c.png",
					"max_316": "https://mir-s3-cdn-cf.behance.net/project_modules/max_316/74442b96673831.5eb397b514b7c.png",
					"max_158": "https://mir-s3-cdn-cf.behance.net/project_modules/max_158/74442b96673831.5eb397b514b7c.png",
					"disp": "https://mir-s3-cdn-cf.behance.net/project_modules/disp/74442b96673831.5eb397b514b7c.png",
					"max_1240": "https://mir-s3-cdn-cf.behance.net/project_modules/hd/74442b96673831.5eb397b514b7c.png",
					"max_1920": "https://mir-s3-cdn-cf.behance.net/project_modules/fs/74442b96673831.5eb397b514b7c.png",
					"max_1200": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/74442b96673831.5eb397b514b7c.png",
					"original": "https://mir-s3-cdn-cf.behance.net/project_modules/source/74442b96673831.5eb397b514b7c.png"
				},
				"dimensions": {
					"max_632": {
						"width": 1292,
						"height": 632
					},
					"max_316": {
						"width": 646,
						"height": 316
					},
					"max_158": {
						"width": 323,
						"height": 158
					},
					"disp": {
						"width": 600,
						"height": 293
					},
					"max_1240": {
						"width": 1240,
						"height": 606
					},
					"max_1920": {
						"width": 1366,
						"height": 668
					},
					"max_1200": {
						"width": 1200,
						"height": 587
					},
					"original": {
						"width": 1366,
						"height": 668
					}
				},
				"is_image": true,
				"is_video": false,
				"is_embed": false,
				"is_text": false,
				"is_audio": false,
				"is_grid": false,
				"picture": {
					"sources": [
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/disp/74442b96673831.5eb397b514b7c.png",
							"media_query": "(max-width: 633px)",
							"width": 600,
							"height": 293
						},
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/74442b96673831.5eb397b514b7c.png",
							"media_query": "(min-width: 634px) and (max-width: 1233px)",
							"width": 1200,
							"height": 587
						},
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/fs/74442b96673831.5eb397b514b7c.png",
							"media_query": "(min-width: 1434px) and (max-width: 1953px)",
							"width": 1366,
							"height": 668
						}
					],
					"img": {
						"src": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/74442b96673831.5eb397b514b7c.png",
						"width": 1200,
						"height": 587
					}
				},
				"picture_largest": {
					"sources": [
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/disp/74442b96673831.5eb397b514b7c.png",
							"media_query": "(max-width: 633px)",
							"width": 600,
							"height": 293
						},
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/74442b96673831.5eb397b514b7c.png",
							"media_query": "(min-width: 634px) and (max-width: 1233px)",
							"width": 1200,
							"height": 587
						},
						{
							"srcset": "https://mir-s3-cdn-cf.behance.net/project_modules/fs/74442b96673831.5eb397b514b7c.png",
							"media_query": "(min-width: 1434px) and (max-width: 1953px)",
							"width": 1366,
							"height": 668
						}
					],
					"img": {
						"src": "https://mir-s3-cdn-cf.behance.net/project_modules/fs/74442b96673831.5eb397b514b7c.png",
						"width": 1366,
						"height": 668
					}
				},
				"aspect_ratio": "48.83%",
				"width": 600,
				"height": 293,
				"exif": [],
				"is_lazy": false
			}
		],
		"name": "SpyTool | social ads intelligence",
		"owners": [
			{
				"id": 14044943,
				"first_name": "Stefanos",
				"last_name": "Chrs",
				"username": "stefanoschrs",
				"city": "Nantes",
				"state": "",
				"country": "France",
				"location": "Nantes, France",
				"company": "",
				"occupation": "Fullstack Developer",
				"created_on": 1432479362,
				"url": "https://www.behance.net/stefanoschrs",
				"images": {
					"50": "https://mir-s3-cdn-cf.behance.net/user/50/b9676514044943.5cd046f4e56d4.jpg",
					"100": "https://mir-s3-cdn-cf.behance.net/user/100/b9676514044943.5cd046f4e56d4.jpg",
					"115": "https://mir-s3-cdn-cf.behance.net/user/115/b9676514044943.5cd046f4e56d4.jpg",
					"138": "https://mir-s3-cdn-cf.behance.net/user/138/b9676514044943.5cd046f4e56d4.jpg",
					"230": "https://mir-s3-cdn-cf.behance.net/user/230/b9676514044943.5cd046f4e56d4.jpg",
					"276": "https://mir-s3-cdn-cf.behance.net/user/276/b9676514044943.5cd046f4e56d4.jpg"
				},
				"display_name": "Stefanos Chrs",
				"fields": [
					"UI/UX",
					"Web Design",
					"Web Development"
				],
				"has_default_image": 0,
				"website": "https://stefanoschrs.com",
				"banner_image_url": "https://mir-s3-cdn-cf.behance.net/v1/assets/49db20fdf321f25053e4bcf6e0e0e79c/e7f5733d-edf6-4d80-9067-7ae11ab959e9_rwc_281x0x2637x410x3200.png?h=6380f534563881fd83fa8e9dd1373f72",
				"stats": {
					"followers": 4,
					"following": 6,
					"appreciations": 6,
					"views": 281,
					"comments": 0
				},
				"location_link": "/search?content=users&country=FR&city=Nantes",
				"has_talent_info": true
			}
		],
		"privacy": "public",
		"published_on": 1588828272,
		"schools": [],
		"short_url": "http://be.net/gallery/96673831/SpyTool-social-ads-intelligence",
		"slug": "SpyTool-social-ads-intelligence",
		"stats": {
			"views": 2,
			"appreciations": 1,
			"comments": 1
		},
		"styles": {
			"text": {
				"title": {
					"font_family": "arial,helvetica,sans-serif",
					"font_weight": "bold",
					"color": "#3B3B3B",
					"text_align": "left",
					"line_height": "1.4em",
					"font_size": "16px",
					"text_decoration": "none",
					"font_style": "normal",
					"display": "inline",
					"text_transform": "none"
				},
				"subtitle": {
					"font_family": "arial,helvetica,sans-serif",
					"font_weight": "normal",
					"color": "#3B3B3B",
					"text_align": "left",
					"line_height": "1.4em",
					"font_size": "14px",
					"text_decoration": "none",
					"font_style": "normal",
					"display": "inline",
					"text_transform": "none"
				},
				"paragraph": {
					"font_family": "arial,helvetica,sans-serif",
					"font_weight": "normal",
					"color": "#3B3B3B",
					"text_align": "left",
					"line_height": "1.4em",
					"font_size": "14px",
					"text_decoration": "none",
					"font_style": "normal",
					"display": "inline",
					"text_transform": "none"
				},
				"caption": {
					"font_family": "arial,helvetica,sans-serif",
					"font_weight": "normal",
					"color": "#3B3B3B",
					"text_align": "left",
					"line_height": "1.4em",
					"font_size": "11px",
					"text_decoration": "none",
					"font_style": "italic",
					"display": "block",
					"text_transform": "none"
				},
				"link": {
					"font_family": "arial,helvetica,sans-serif",
					"font_weight": "normal",
					"color": "#1769FF",
					"text_align": "left",
					"line_height": "1.4em",
					"font_size": "14px",
					"text_decoration": "none",
					"font_style": "normal",
					"display": "inline",
					"text_transform": "none"
				}
			},
			"background": {
				"color": "EFEFEF"
			},
			"spacing": {
				"project": {
					"top_margin": 50
				},
				"modules": {
					"bottom_margin": 60
				}
			},
			"dividers": {
				"font_size": "1px",
				"line_height": "1px",
				"height": "1px",
				"border_color": "#000",
				"margin": "-1px auto 0",
				"position": "relative",
				"top": "50%",
				"border_width": "1px 0px 0px 0px",
				"border_style": "dashed"
			}
		},
		"tags": [
			{
				"id": 1203773,
				"title": "angular",
				"category": "101",
				"url": "/search?content=projects&search=angular"
			},
			{
				"id": 196831115,
				"title": "facebook",
				"category": "101",
				"url": "/search?content=projects&search=facebook"
			},
			{
				"id": 1015007,
				"title": "go",
				"category": "101",
				"url": "/search?content=projects&search=go"
			},
			{
				"id": 4664339,
				"title": "Ionic",
				"category": "101",
				"url": "/search?content=projects&search=Ionic"
			},
			{
				"id": 1609955,
				"title": "nodejs",
				"category": "101",
				"url": "/search?content=projects&search=nodejs"
			}
		],
		"teams": [],
		"tools": [],
		"tools_by_synonym": [],
		"tools_without_synonym": [],
		"url": "https://www.behance.net/gallery/96673831/SpyTool-social-ads-intelligence",
		"visible_to": []
	}
]
