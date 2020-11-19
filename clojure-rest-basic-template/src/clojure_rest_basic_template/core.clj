(ns clojure-rest-basic-template.core
  (:gen-class)
  (:require [ring.adapter.jetty :as jetty]
            [ring.middleware.reload :refer [wrap-reload]]
            [ring.middleware.params :refer [wrap-params]]
            [compojure.core :refer [defroutes ANY GET POST PUT DELETE]]
            [compojure.route :refer [not-found]]
            [ring.handler.dump :refer [handle-dump]]))

(defn greet [req]
  {:status 200
   :body "Hello World!\n
          If you see this, your Clojure Ring server is working fine.\n
          other endpoints to checkout: /request, /sample, /notfound"
   :headers {}})
(defn sample [req]
  {:status 200
   :body "Hello world"
   :headers {}})

; REST routes
(defroutes routes
  (GET "/" [] greet)
  (GET "/request" [] handle-dump)
  (GET "/sample" [] sample)
  (not-found "Page not found"))

(defn wrap-server [hdlr]
  (fn [req]
    (assoc-in (hdlr req) [:headers "Server"] "Template REST Server")))

(def app
  (wrap-server  (wrap-params routes)))

(defn -main
  []
  (jetty/run-jetty (wrap-reload app) {:port (Integer. 8000)}))
