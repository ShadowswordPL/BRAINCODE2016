//
//  ViewController.swift
//  ClassList
//
//  Created by Tomasz Bąk on 18.03.2016.
//  Copyright © 2016 Cornucopia of Code. All rights reserved.
//

import UIKit

class PhotoViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    @IBAction func check(sender: AnyObject) {
        let picker = UIImagePickerController()
        picker.sourceType = .Camera
        picker.delegate = self
        presentViewController(picker, animated: true, completion: nil)
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

extension PhotoViewController: UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    func imagePickerController(picker: UIImagePickerController, didFinishPickingImage image: UIImage, editingInfo: [String : AnyObject]?) {
        self.dismissViewControllerAnimated(true) { [weak self] in
            self?.performSegueWithIdentifier("show list", sender: nil)
        }
    }
    
    func imagePickerControllerDidCancel(picker: UIImagePickerController) {
        self.dismissViewControllerAnimated(true, completion: nil)
    }
}

