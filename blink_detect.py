{"payload":{"allShortcutsEnabled":false,"fileTree":{"":{"items":[{"name":"README.md","path":"README.md","contentType":"file"},{"name":"blink_detect.py","path":"blink_detect.py","contentType":"file"},{"name":"eye_blink_game.py","path":"eye_blink_game.py","contentType":"file"},{"name":"haarcascade_eye_tree_eyeglasses.xml","path":"haarcascade_eye_tree_eyeglasses.xml","contentType":"file"},{"name":"haarcascade_frontalface_default.xml","path":"haarcascade_frontalface_default.xml","contentType":"file"}],"totalCount":5}},"fileTreeProcessingTime":2.1140619999999997,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":264300236,"defaultBranch":"master","name":"Eye-blink-detection-game","ownerLogin":"infoaryan","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2020-05-15T21:13:50.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/56125346?v=4","public":true,"private":false,"isOrgOwned":false},"refInfo":{"name":"master","listCacheKey":"v0:1589577269.0","canEdit":false,"refType":"branch","currentOid":"ca743ea3becaf90fcab83c4612a9241ce8c7b297"},"path":"blink_detect.py","currentUser":null,"blob":{"rawLines":["#All the imports go here","import numpy as np","import cv2","","#Initializing the face and eye cascade classifiers from xml files","face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')","eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')","","#Variable store execution state","first_read = True","","#Starting the video capture","cap = cv2.VideoCapture(0)","ret,img = cap.read()","","while(ret):","    ret,img = cap.read()","    #Coverting the recorded image to grayscale","    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)","    #Applying filter to remove impurities","    gray = cv2.bilateralFilter(gray,5,1,1)","","    #Detecting the face for region of image to be fed to eye classifier","    faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(200,200))","    if(len(faces)>0):","        for (x,y,w,h) in faces:","            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)","","            #roi_face is face which is input to eye classifier","            roi_face = gray[y:y+h,x:x+w]","            roi_face_clr = img[y:y+h,x:x+w]","            eyes = eye_cascade.detectMultiScale(roi_face,1.3,5,minSize=(50,50))","","            #Examining the length of eyes object for eyes","            if(len(eyes)>=2):","                #Check if program is running for detection ","                if(first_read):","                    cv2.putText(img, \"Eye detected press s to begin\", (70,70), cv2.FONT_HERSHEY_PLAIN, 3,(0,255,0),2)","                else:","                    cv2.putText(img, \"Eyes open!\", (70,70), cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255),2)","            else:","                if(first_read):","                    #To ensure if the eyes are present before starting","                    cv2.putText(img, \"No eyes detected\", (70,70), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255),2)","                else:","                    #This will print on console and restart the algorithm","                    print(\"Blink detected--------------\")","                    cv2.waitKey(3000)","                    first_read=True","            ","    else:","        cv2.putText(img,\"No face detected\",(100,100),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0),2)","","    #Controlling the algorithm with keys","    cv2.imshow('img',img)","    a = cv2.waitKey(1)","    if(a==ord('q')):","        break","    elif(a==ord('s') and first_read):","        #This will start the detection","        first_read = False","","cap.release()","cv2.destroyAllWindows()"],"stylingDirectives":[[{"start":0,"end":24,"cssClass":"pl-c"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":12,"cssClass":"pl-s1"},{"start":13,"end":15,"cssClass":"pl-k"},{"start":16,"end":18,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"}],[],[{"start":0,"end":65,"cssClass":"pl-c"}],[{"start":0,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":18,"cssClass":"pl-s1"},{"start":19,"end":36,"cssClass":"pl-v"},{"start":37,"end":74,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":17,"cssClass":"pl-s1"},{"start":18,"end":35,"cssClass":"pl-v"},{"start":36,"end":73,"cssClass":"pl-s"}],[],[{"start":0,"end":31,"cssClass":"pl-c"}],[{"start":0,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":17,"cssClass":"pl-c1"}],[],[{"start":0,"end":27,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":5,"cssClass":"pl-c1"},{"start":6,"end":9,"cssClass":"pl-s1"},{"start":10,"end":22,"cssClass":"pl-v"},{"start":23,"end":24,"cssClass":"pl-c1"}],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":13,"cssClass":"pl-s1"},{"start":14,"end":18,"cssClass":"pl-en"}],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":9,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":17,"cssClass":"pl-s1"},{"start":18,"end":22,"cssClass":"pl-en"}],[{"start":4,"end":46,"cssClass":"pl-c"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":14,"cssClass":"pl-s1"},{"start":15,"end":23,"cssClass":"pl-en"},{"start":24,"end":27,"cssClass":"pl-s1"},{"start":28,"end":31,"cssClass":"pl-s1"},{"start":32,"end":46,"cssClass":"pl-v"}],[{"start":4,"end":41,"cssClass":"pl-c"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":14,"cssClass":"pl-s1"},{"start":15,"end":30,"cssClass":"pl-en"},{"start":31,"end":35,"cssClass":"pl-s1"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":40,"end":41,"cssClass":"pl-c1"}],[],[{"start":4,"end":71,"cssClass":"pl-c"}],[{"start":4,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":24,"cssClass":"pl-s1"},{"start":25,"end":41,"cssClass":"pl-en"},{"start":42,"end":46,"cssClass":"pl-s1"},{"start":48,"end":51,"cssClass":"pl-c1"},{"start":53,"end":54,"cssClass":"pl-c1"},{"start":55,"end":62,"cssClass":"pl-s1"},{"start":62,"end":63,"cssClass":"pl-c1"},{"start":64,"end":67,"cssClass":"pl-c1"},{"start":68,"end":71,"cssClass":"pl-c1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-en"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":18,"end":19,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":13,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":25,"end":30,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":21,"cssClass":"pl-s1"},{"start":22,"end":31,"cssClass":"pl-en"},{"start":32,"end":35,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-c1"},{"start":45,"end":46,"cssClass":"pl-s1"},{"start":47,"end":48,"cssClass":"pl-s1"},{"start":48,"end":49,"cssClass":"pl-c1"},{"start":49,"end":50,"cssClass":"pl-s1"},{"start":53,"end":54,"cssClass":"pl-c1"},{"start":55,"end":58,"cssClass":"pl-c1"},{"start":59,"end":60,"cssClass":"pl-c1"},{"start":62,"end":63,"cssClass":"pl-c1"}],[],[{"start":12,"end":62,"cssClass":"pl-c"}],[{"start":12,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-c1"},{"start":32,"end":33,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-s1"},{"start":36,"end":37,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":38,"end":39,"cssClass":"pl-s1"}],[{"start":12,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":30,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-c1"},{"start":41,"end":42,"cssClass":"pl-s1"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":30,"cssClass":"pl-s1"},{"start":31,"end":47,"cssClass":"pl-en"},{"start":48,"end":56,"cssClass":"pl-s1"},{"start":57,"end":60,"cssClass":"pl-c1"},{"start":61,"end":62,"cssClass":"pl-c1"},{"start":63,"end":70,"cssClass":"pl-s1"},{"start":70,"end":71,"cssClass":"pl-c1"},{"start":72,"end":74,"cssClass":"pl-c1"},{"start":75,"end":77,"cssClass":"pl-c1"}],[],[{"start":12,"end":57,"cssClass":"pl-c"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":15,"end":18,"cssClass":"pl-en"},{"start":19,"end":23,"cssClass":"pl-s1"},{"start":24,"end":26,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"}],[{"start":16,"end":59,"cssClass":"pl-c"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":19,"end":29,"cssClass":"pl-s1"}],[{"start":20,"end":23,"cssClass":"pl-s1"},{"start":24,"end":31,"cssClass":"pl-en"},{"start":32,"end":35,"cssClass":"pl-s1"},{"start":37,"end":68,"cssClass":"pl-s"},{"start":71,"end":73,"cssClass":"pl-c1"},{"start":74,"end":76,"cssClass":"pl-c1"},{"start":79,"end":82,"cssClass":"pl-s1"},{"start":83,"end":101,"cssClass":"pl-v"},{"start":103,"end":104,"cssClass":"pl-c1"},{"start":106,"end":107,"cssClass":"pl-c1"},{"start":108,"end":111,"cssClass":"pl-c1"},{"start":112,"end":113,"cssClass":"pl-c1"},{"start":115,"end":116,"cssClass":"pl-c1"}],[{"start":16,"end":20,"cssClass":"pl-k"}],[{"start":20,"end":23,"cssClass":"pl-s1"},{"start":24,"end":31,"cssClass":"pl-en"},{"start":32,"end":35,"cssClass":"pl-s1"},{"start":37,"end":49,"cssClass":"pl-s"},{"start":52,"end":54,"cssClass":"pl-c1"},{"start":55,"end":57,"cssClass":"pl-c1"},{"start":60,"end":63,"cssClass":"pl-s1"},{"start":64,"end":82,"cssClass":"pl-v"},{"start":84,"end":85,"cssClass":"pl-c1"},{"start":87,"end":90,"cssClass":"pl-c1"},{"start":91,"end":94,"cssClass":"pl-c1"},{"start":95,"end":98,"cssClass":"pl-c1"},{"start":100,"end":101,"cssClass":"pl-c1"}],[{"start":12,"end":16,"cssClass":"pl-k"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":19,"end":29,"cssClass":"pl-s1"}],[{"start":20,"end":70,"cssClass":"pl-c"}],[{"start":20,"end":23,"cssClass":"pl-s1"},{"start":24,"end":31,"cssClass":"pl-en"},{"start":32,"end":35,"cssClass":"pl-s1"},{"start":37,"end":55,"cssClass":"pl-s"},{"start":58,"end":60,"cssClass":"pl-c1"},{"start":61,"end":63,"cssClass":"pl-c1"},{"start":66,"end":69,"cssClass":"pl-s1"},{"start":70,"end":88,"cssClass":"pl-v"},{"start":90,"end":91,"cssClass":"pl-c1"},{"start":93,"end":94,"cssClass":"pl-c1"},{"start":95,"end":96,"cssClass":"pl-c1"},{"start":97,"end":100,"cssClass":"pl-c1"},{"start":102,"end":103,"cssClass":"pl-c1"}],[{"start":16,"end":20,"cssClass":"pl-k"}],[{"start":20,"end":73,"cssClass":"pl-c"}],[{"start":20,"end":25,"cssClass":"pl-en"},{"start":26,"end":56,"cssClass":"pl-s"}],[{"start":20,"end":23,"cssClass":"pl-s1"},{"start":24,"end":31,"cssClass":"pl-en"},{"start":32,"end":36,"cssClass":"pl-c1"}],[{"start":20,"end":30,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":31,"end":35,"cssClass":"pl-c1"}],[],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":19,"cssClass":"pl-en"},{"start":20,"end":23,"cssClass":"pl-s1"},{"start":24,"end":42,"cssClass":"pl-s"},{"start":44,"end":47,"cssClass":"pl-c1"},{"start":48,"end":51,"cssClass":"pl-c1"},{"start":53,"end":56,"cssClass":"pl-s1"},{"start":57,"end":75,"cssClass":"pl-v"},{"start":77,"end":78,"cssClass":"pl-c1"},{"start":81,"end":82,"cssClass":"pl-c1"},{"start":83,"end":86,"cssClass":"pl-c1"},{"start":87,"end":88,"cssClass":"pl-c1"},{"start":90,"end":91,"cssClass":"pl-c1"}],[],[{"start":4,"end":40,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":20,"cssClass":"pl-s"},{"start":21,"end":24,"cssClass":"pl-s1"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":7,"cssClass":"pl-c1"},{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":19,"cssClass":"pl-en"},{"start":20,"end":21,"cssClass":"pl-c1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":8,"cssClass":"pl-s1"},{"start":8,"end":10,"cssClass":"pl-c1"},{"start":10,"end":13,"cssClass":"pl-en"},{"start":14,"end":17,"cssClass":"pl-s"}],[{"start":8,"end":13,"cssClass":"pl-k"}],[{"start":4,"end":8,"cssClass":"pl-k"},{"start":9,"end":10,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":12,"end":15,"cssClass":"pl-en"},{"start":16,"end":19,"cssClass":"pl-s"},{"start":21,"end":24,"cssClass":"pl-c1"},{"start":25,"end":35,"cssClass":"pl-s1"}],[{"start":8,"end":38,"cssClass":"pl-c"}],[{"start":8,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-c1"}],[],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":11,"cssClass":"pl-en"}],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":21,"cssClass":"pl-en"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/infoaryan/Eye-blink-detection-game/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/infoaryan/Eye-blink-detection-game/security/dependabot","repoSecurityAndAnalysisPath":"/infoaryan/Eye-blink-detection-game/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"blink_detect.py","displayUrl":"https://github.com/infoaryan/Eye-blink-detection-game/blob/master/blink_detect.py?raw=true","headerInfo":{"blobSize":"2.32 KB","deleteInfo":{"deletePath":null,"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"4f5fd13","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Finfoaryan%2FEye-blink-detection-game%2Fblob%2Fmaster%2Fblink_detect.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"64","truncatedSloc":"54"},"mode":"file"},"image":false,"isCodeownersFile":null,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","large":false,"loggedIn":false,"newDiscussionPath":"/infoaryan/Eye-blink-detection-game/discussions/new","newIssuePath":"/infoaryan/Eye-blink-detection-game/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/infoaryan/Eye-blink-detection-game/blob/master/blink_detect.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/infoaryan/Eye-blink-detection-game/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"infoaryan","repoName":"Eye-blink-detection-game","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"face_cascade","kind":"constant","identStart":122,"identEnd":134,"extentStart":122,"extentEnd":197,"fullyQualifiedName":"face_cascade","identUtf16":{"start":{"lineNumber":5,"utf16Col":0},"end":{"lineNumber":5,"utf16Col":12}},"extentUtf16":{"start":{"lineNumber":5,"utf16Col":0},"end":{"lineNumber":5,"utf16Col":75}}},{"name":"eye_cascade","kind":"constant","identStart":198,"identEnd":209,"extentStart":198,"extentEnd":272,"fullyQualifiedName":"eye_cascade","identUtf16":{"start":{"lineNumber":6,"utf16Col":0},"end":{"lineNumber":6,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":6,"utf16Col":0},"end":{"lineNumber":6,"utf16Col":74}}},{"name":"first_read","kind":"constant","identStart":306,"identEnd":316,"extentStart":306,"extentEnd":323,"fullyQualifiedName":"first_read","identUtf16":{"start":{"lineNumber":9,"utf16Col":0},"end":{"lineNumber":9,"utf16Col":10}},"extentUtf16":{"start":{"lineNumber":9,"utf16Col":0},"end":{"lineNumber":9,"utf16Col":17}}},{"name":"cap","kind":"constant","identStart":353,"identEnd":356,"extentStart":353,"extentEnd":378,"fullyQualifiedName":"cap","identUtf16":{"start":{"lineNumber":12,"utf16Col":0},"end":{"lineNumber":12,"utf16Col":3}},"extentUtf16":{"start":{"lineNumber":12,"utf16Col":0},"end":{"lineNumber":12,"utf16Col":25}}}]}},"copilotUserAccess":null,"csrf_tokens":{"/infoaryan/Eye-blink-detection-game/branches":{"post":"XSRC17wVlsnxMZsQAIGDmus9-_SWroVtC059TeP2WXVryP-VUKVkDIATtOI6AmUJL0_NoGrktEdKCh9MyLCgCA"}}},"title":"Eye-blink-detection-game/blink_detect.py at master · infoaryan/Eye-blink-detection-game","locale":"en"}