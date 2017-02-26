/**
 * Created by Jonny on 2017/2/26.
 */
package {
import flash.display.Sprite;
import flash.events.Event;
import flash.net.URLLoader;
import flash.net.URLLoaderDataFormat;
import flash.net.URLRequest;
import flash.utils.ByteArray;
import flash.utils.Dictionary;

public class Main extends Sprite {
    private var _urlLoader:URLLoader;
    public function Main() {
        super();

        this.addEventListener(Event.ADDED_TO_STAGE , onAddedToStageHandler);
    }

    private function onAddedToStageHandler(event:Event):void
    {
        this.addEventListener(Event.ADDED_TO_STAGE , onAddedToStageHandler);

        _urlLoader = new URLLoader();
        _urlLoader.load(new URLRequest("output.txt"));
        _urlLoader.addEventListener(Event.COMPLETE, loadComplete);
    }

    private function loadComplete(event:Event):void
    {
        var data:String = event.target.data;
        var json:Object = JSON.parse(data);
        var fileCount:int = 0;
        for (var fileName:String in json) {
            fileCount ++;
            trace(fileName ,"   MD5:",json[fileName]);
        }
        trace("文件总数 " + fileCount);
    }
}
}
