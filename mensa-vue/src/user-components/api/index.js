import axios from 'axios'

export default{
    fetchMenu (method, params, data){
        if(method === 'post'){
            return ajax('http://localhost:8000/api/menu/', method, {data})
            // return ajax('api/notes/', 'get', null, null)
        }else{
            return ajax('http://localhost:8000/api/menu/', 'get', {})
        }
    },
    fetchNotes (method, params, data){
        if(method === 'post'){
            return ajax('http://localhost:8000/api/notes/', method, {data})
            // return ajax('api/notes/', 'get', null, null)
        }else{
            return ajax('http://localhost:8000/api/notes/', 'get', {})
        }
    }
}

/**
 * @param url
 * @param method
 * @param params
 * @param data
 * @returns
 */

 function ajax(url, method, options){
    if(options !== undefined){
        var {params = {}, data = {}} = options
    }else{
        params = data = {}
    }
    return new Promise((resolve, reject) =>{
        axios({
            url,
            method,
            params,
            data
        }).then(res => {
            resolve(res)
        }, res => {
            reject(res)
        })
    })
 }